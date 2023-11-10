from functools import partial
from typing import Dict, Optional
from pathlib import Path
from sys import argv
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from re import compile
from json import dump

from p_tqdm import p_uimap
from numpy import nan

from eis1600.helper.repo import TOPO_TRAINING_REPO, TRAINING_DATA_REPO
from eis1600.markdown.md_to_bio import md_to_bio
from eis1600.processing.preprocessing import get_yml_and_miu_df
from eis1600.toponyms.toponym_categories import TOPONYM_CATEGORIES

CATS = ''.join(TOPONYM_CATEGORIES)
TOP_PATTERN = compile(r"T(?P<num_tokens>\d)(?P<cat>[" + CATS + "])")


def reconstruct_automated_tag(row) -> str:
    return 'ÜT' + row['num_tokens'] + row['cat']


def get_tops_true(file: str, label_dict: Dict, keep_automatic_tags: Optional[bool] = False) -> Dict:
    with open(file, 'r', encoding='utf-8') as miu_file_object:
        yml_handler, df = get_yml_and_miu_df(miu_file_object, keep_automatic_tags)

    s_notna = df['TAGS_LISTS'].loc[df['TAGS_LISTS'].notna()].apply(lambda tag_list: ','.join(tag_list))
    df_true = s_notna.str.extract(TOP_PATTERN).dropna(how='all')
    tops = df_true.apply(reconstruct_automated_tag, axis=1)
    tops.name = 'TOPS_TRUE'

    if not tops.empty:
        df = df.join(tops)
    else:
        df['TOPS_TRUE'] = nan

    bio_tags = md_to_bio(
            df[['TOKENS', 'TOPS_TRUE']],
            'TOPS_TRUE',
            TOP_PATTERN,
            'TO',
            label_dict
    )

    return bio_tags


def main():
    arg_parser = ArgumentParser(
            prog=argv[0], formatter_class=RawDescriptionHelpFormatter,
            description='''Script to annotate onomastic information in gold-standard MIUs.'''
    )
    arg_parser.add_argument('-D', '--debug', action='store_true')
    arg_parser.add_argument('-K', '--keep', action='store_true')

    args = arg_parser.parse_args()
    debug = args.debug
    keep = args.keep

    with open(TRAINING_DATA_REPO + 'gold_standard.txt', 'r', encoding='utf-8') as fh:
        files_txt = fh.read().splitlines()

    infiles = [TRAINING_DATA_REPO + 'gold_standard_topo/' + file for file in files_txt if Path(
            TRAINING_DATA_REPO + 'gold_standard_topo/' + file).exists()]

    label_dict = get_bio_dict('TO', TOPONYM_CATEGORIES)

    res = []
    if debug:
        for file in infiles[20:40]:
            print(file)
            res.append(get_tops_true(file, label_dict))
    else:
        res += p_uimap(partial(get_tops_true, label_dict=label_dict, keep_automatic_tags=keep), infiles)

    with open(TOPO_TRAINING_REPO + 'toponyms_category_training_data.json', 'w', encoding='utf-8') as fh:
        dump(res, fh, indent=4, ensure_ascii=False)

    print('Done')
