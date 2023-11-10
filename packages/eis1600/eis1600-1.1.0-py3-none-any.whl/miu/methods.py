from glob import glob
from logging import Logger
from os.path import splitext, split, exists
from typing import List, Optional
from pathlib import Path

from eis1600.onomastics.methods import nasab_annotate_miu

from eis1600.dates.methods import date_annotate_miu_text
from eis1600.miu.HeadingTracker import HeadingTracker
from eis1600.processing.preprocessing import get_yml_and_miu_df
from eis1600.processing.postprocessing import write_updated_miu_to_file
from eis1600.nlp.utils import camel2md_as_list, annotate_miu_text
from eis1600.miu.yml_handling import create_yml_header, extract_yml_header_and_text
from eis1600.helper.markdown_patterns import CATEGORY_PATTERN, HEADER_END_PATTERN, HEADING_PATTERN, MIU_TAG_PATTERN, \
    MIU_UID_PATTERN, PAGE_TAG_PATTERN


def disassemble_text(infile: str, out_path: str, verbose: Optional[bool] = None) -> None:
    """Disassemble text into MIU files.

    Retrieve MIU files by disassembling the text based on the EIS1600 mARkdown.
    :param str infile: Path to the file which is to be disassembled.
    :param str out_path: Path to the MIU repo.
    :param bool verbose: If True outputs a notification of the file which is currently processed, optional.
    """

    heading_tracker = HeadingTracker()
    path, uri = split(infile)
    uri, ext = splitext(uri)
    author, work, text = uri.split('.')
    path = out_path + '/'.join([author, '.'.join([author, work])]) + '/'
    ids_file = path + uri + '.IDs'
    yml_status = path + uri + '.STATUS.yml'
    yml_data = path + uri + '.YAMLDATA.yml'
    miu_dir = Path(path + 'MIUs/')
    uid = ''
    miu_text = ''
    yml_header = ''

    if verbose:
        print(f'Disassemble {uri}')

    miu_dir.mkdir(parents=True, exist_ok=True)
    miu_uri = miu_dir.__str__() + '/' + uri + '.'

    mal_formatted = []

    with open(infile, 'r', encoding='utf8') as text:
        with open(ids_file, 'w', encoding='utf8') as ids_tree:
            with open(yml_data, 'w', encoding='utf-8') as yml_data_fh:
                for text_line in iter(text):
                    if HEADER_END_PATTERN.match(text_line):
                        uid = 'header'
                        miu_text += text_line
                        with open(miu_uri + uid + '.EIS1600', 'w', encoding='utf8') as miu_file:
                            miu_file.write(miu_text + '\n')
                            ids_tree.write(uid + '\n')
                        miu_text = ''
                        uid = 'preface'
                        next(text)  # Skip empty line after header
                    elif MIU_UID_PATTERN.match(text_line):
                        if HEADING_PATTERN.match(text_line):
                            m = HEADING_PATTERN.match(text_line)
                            heading_text = m.group('heading')
                            if PAGE_TAG_PATTERN.search(heading_text):
                                heading_text = PAGE_TAG_PATTERN.sub('', heading_text)
                            heading_tracker.track_headings(len(m.group('level')), heading_text)
                        if miu_text:
                            # Do not create a preface MIU file if there is no preface
                            with open(miu_uri + uid + '.EIS1600', 'w', encoding='utf8') as miu_file:
                                miu_file.write(miu_text + '\n')
                                ids_tree.write(uid + '\n')
                            yml_data_fh.write('#' + uid + '\n---\n' + yml_header)
                        m = MIU_TAG_PATTERN.match(text_line)
                        uid = m.group('UID')
                        try:
                            category = CATEGORY_PATTERN.search(m.group('category')).group(0)
                        except AttributeError:
                            mal_formatted.append(m.group('category'))
                        yml_header = create_yml_header(category, heading_tracker.get_curr_state())
                        miu_text = yml_header
                        miu_text += text_line
                    else:
                        miu_text += text_line

                    if PAGE_TAG_PATTERN.search(text_line):
                        heading_tracker.track_pages(PAGE_TAG_PATTERN.search(text_line).group(0))

                # last MIU needs to be written to file when the for-loop is finished
                with open(miu_uri + uid + '.EIS1600', 'w', encoding='utf8') as miu_file:
                    miu_file.write(miu_text + '\n')
                    ids_tree.write(uid + '\n')
                yml_data_fh.write('#' + uid + '\n---\n' + yml_header + '\n\n')

                if mal_formatted:
                    print('Something seems to be mal-formatted, check:')
                    print(infile + '\n')
                    for elem in mal_formatted:
                        print(elem)

    with open(yml_status, 'w', encoding='utf8') as status_file:
        status_file.write('STATUS   : DISASSEMBLED')


def reassemble_text(infile: str, out_path: str, verbose: Optional[bool] = None) -> None:
    """Reassemble text from MIU files.

    Reassemble text from MIU files.
    :param str infile: Path to the IDs file of the text to reassemble from MIU files.
    :param str out_path: Path to the TEXT repo.
    :param bool verbose: If True outputs a notification of the file which is currently processed, optional.
    """
    file_path, uri = split(infile)
    file_path += '/'
    uri, ext = splitext(uri)
    author, work, text = uri.split('.')
    path = out_path + '/'.join([author, '.'.join([author, work])]) + '/' + uri
    ids = []

    if verbose:
        print(f'Reassemble {uri}')

    with open(file_path + uri + '.IDs', 'r', encoding='utf-8') as ids_file:
        ids.extend([line[:-1] for line in ids_file.readlines()])

    with open(path + '.EIS1600', 'w', encoding='utf-8') as text_file:
        with open(file_path + uri + '.YAMLDATA.yml', 'w', encoding='utf-8') as yml_data:
            for i, miu_id in enumerate(ids):
                miu_file_path = file_path + 'MIUs/' + uri + '.' + miu_id + '.EIS1600'
                with open(miu_file_path, 'r', encoding='utf-8') as miu_file_object:
                    yml_header, text = extract_yml_header_and_text(miu_file_object, i == 0)
                text_file.write(text)
                yml_data.write('#' + miu_id + '\n---\n' + yml_header + '\n\n')


def get_mius(infile: str) -> List[str]:
    """Get a list of paths to all MIU files from the infile text (including the HEADER MIU)

    :param infile: URI of text for which all MIU files are retrieved
    :return List[str]: A List of path to all the MIU files from the text
    """
    file_path, uri = split(infile)
    uri, ext = splitext(uri)
    file_path += '/'
    ids = []
    mius = []

    with open(infile, 'r', encoding='utf-8') as ids_file:
        ids.extend([line[:-1] for line in ids_file.readlines()])

    for i, miu_id in enumerate(ids):
        mius.extend(glob(file_path + 'MIUs/' + uri + '.' + miu_id + '.EIS1600'))

    return mius


def annotate_miu_file(path: str, logger: Logger = None, tsv_path=None, output_path=None, force_annotation=False):
    if output_path is None:
        output_path = path
    if tsv_path is None:
        tsv_path = path.replace('.EIS1600', '.tsv')

    # if the file is already annotated, do nothing
    if exists(tsv_path) and not force_annotation:
        return

    with open(path, 'r+', encoding='utf-8') as miu_file_object:
        # 1. open miu file and disassemble the file to its parts
        yml_handler, df = get_yml_and_miu_df(miu_file_object)

        # 2. annotate NEs and lemmatize
        df['NER_LABELS'], df['LEMMAS'], df['POS_TAGS'] = annotate_miu_text(df)

        # 3. convert cameltools labels format to markdown format
        df['NER_TAGS'] = camel2md_as_list(df['NER_LABELS'].tolist())

        # 4. annotate dates
        df['DATE_TAGS'] = date_annotate_miu_text(df[['TOKENS']], yml_handler)

        # 5. annotate onomastic information
        # TODO Needs to be run after the NASAB END tag was inserted
        df['NASAB_TAGS'] = nasab_annotate_miu(df, yml_handler, path, logger)

        # 6. save csv file
        df.to_csv(tsv_path, index=False, sep='\t')

        # 7. reconstruct the text, populate yml with annotated entities and save it to the output file
        if output_path == path:
            write_updated_miu_to_file(
                miu_file_object, yml_handler, df[['SECTIONS', 'TOKENS', 'TAGS_LISTS', 'NER_TAGS',
                                                 'DATE_TAGS', 'NASAB_TAGS']]
                )
        else:
            with open(output_path, 'w', encoding='utf-8') as out_file_object:
                write_updated_miu_to_file(
                        out_file_object, yml_handler, df[['SECTIONS', 'TOKENS', 'TAGS_LISTS', 'NER_TAGS',
                                                         'DATE_TAGS', 'NASAB_TAGS']]
                )
