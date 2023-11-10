import json
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

from eis1600.helper.my_json_ecoder import MyJSONEncoder
from p_tqdm import p_uimap

from eis1600.processing.preprocessing import get_yml


def main():
    arg_parser = ArgumentParser(
            prog=sys.argv[0], formatter_class=RawDescriptionHelpFormatter,
            description='''Script to generate JSON from MIU YAMLHeaders.'''
    )
    arg_parser.add_argument('-D', '--debug', action='store_true')
    args = arg_parser.parse_args()

    debug = args.debug
    with open('OpenITI_EIS1600_MIUs/gold_standard.txt', 'r', encoding='utf-8') as fh:
        files_txt = fh.read().splitlines()
    infiles = ['OpenITI_EIS1600_MIUs/training_nasab/' + file for file in files_txt if Path(
            'OpenITI_EIS1600_MIUs/training_nasab/' + file
    ).exists()]

    res = []
    if debug:
        for file in infiles[:10]:
            print(file)
            res.append(get_yml(file))
    else:
        res = p_uimap(get_yml, infiles)

    yml_dict = {}
    for path, yml in res:
        yml_dict[path] = yml

    # TODO: Where shall that file be?
    with open('OpenITI_EIS1600_MIUs/gold_standard_yml.json', 'w', encoding='utf-8') as fh:
        json.dump(yml_dict, fh, cls=MyJSONEncoder, indent='\t', ensure_ascii=False)

    print('Done')
