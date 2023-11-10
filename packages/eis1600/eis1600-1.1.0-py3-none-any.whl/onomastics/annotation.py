from glob import glob
from pathlib import Path

import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from functools import partial

from eis1600.helper.logging import setup_logger
from p_tqdm import p_uimap

from eis1600.onomastics.methods import nasab_annotation


def main():
    arg_parser = ArgumentParser(
            prog=sys.argv[0], formatter_class=RawDescriptionHelpFormatter,
            description='''Script to annotate onomastic information in gold-standard MIUs.'''
    )
    arg_parser.add_argument('-D', '--debug', action='store_true')
    arg_parser.add_argument('-T', '--test', action='store_true')

    args = arg_parser.parse_args()
    debug = args.debug
    test = args.test

    with open('OpenITI_EIS1600_MIUs/gold_standard.txt', 'r', encoding='utf-8') as fh:
        files_txt = fh.read().splitlines()
    if test:
        infiles = ['OpenITI_EIS1600_MIUs/training_data/' + file for file in files_txt if Path(
                'OpenITI_EIS1600_MIUs/training_data/' + file).exists()]
    else:
        infiles = glob('OpenITI_EIS1600_MIUs/training_data_nasab_ML2/*.EIS1600')

    logger_nasab = setup_logger('nasab_unknown', 'OpenITI_EIS1600_MIUs/logs/nasab_unknown.log')
    res = []
    if debug:
        for file in infiles:
            print(file)
            res.append(nasab_annotation(file, logger_nasab, test))
    else:
        res += p_uimap(partial(nasab_annotation, logger_nasab=logger_nasab, test=test), infiles)

    with open('gazetteers/tagged.txt', 'w', encoding='utf-8') as fh:
        fh.write('\n\n'.join(res))

    print('Done')
