#!/usr/bin/env python
"""
    This file is part of Polichombr.

    (c) 2018 ANSSI-FR


    Description:
        Creates families
"""


import argparse
from poliapi.mainapi import FamilyModule


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add a family')
    parser.add_argument('api_key',
                        type=str,
                        help="Your API key")
    parser.add_argument('names',
                        type=str,
                        nargs='+',
                        help="The new family name")

    parser.add_argument('--parent', type=str, help='The parent family name')

    parser.add_argument('--tlp', type=int,
                        help="The TLP level,\
                              can be from 1 to 5, \
                              1=TLPWHITE / 5=TLPBLACK")

    args = parser.parse_args()

    fapi = FamilyModule(api_key=args.api_key)

    for fname in args.names:
        if args.parent:
            fid = fapi.create_family(fname, args.parent, args.tlp)
        else:
            fid = fapi.create_family(fname, args.tlp)
        print("Successfully created family with ID %d" % (fid))
