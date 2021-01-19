#!/usr/bin/env python3.8
import argparse
import re
import functools 

import checks

def parse_input(inputdata):
    plist = inputdata.split("\n\n")
    outputlist = []
    for entry in plist:
        entry_dict = {}
        line = entry.replace('\n',' ')
        itemlist = re.findall(r'(\S{3}):(\S+)', line)
        for item in itemlist:
            entry_dict[item[0]] = item[1]
        outputlist.append(entry_dict)

    return outputlist


def check_fields(passport, req_field):
    return False not in [req in passport for req in req_field]


def check_all(passlist, req_fields, hard=False):
    if hard:
        return [checks.apply_all(passport) for passport in passlist]
    else:
        return [check_fields(passport, req_fields) for passport in passlist]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate passports')
    parser.add_argument('inputfile', type=str,
                        help='path to list of passport details')
    args = parser.parse_args()
    
    with open(args.inputfile, 'r') as fh:
        data = parse_input(fh.read())

    req_fields = 'byr iyr eyr hgt hcl ecl pid'.split()

    n_valid = sum(check_all(data, req_fields))

    print(f"Number of valid passports: {n_valid}")

    n_valid_hard = sum(check_all(data, '', hard=True))
    print(f"Number of valid passports (strict tests): {n_valid_hard}")