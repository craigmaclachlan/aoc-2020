#!/usr/bin/env python3.8
import argparse
import re
from collections import Counter

LINE_PATTERN = r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-zA-Z]):\s+(?P<password>[a-zA-Z]+)'


def parse(line):
    reg = re.search(LINE_PATTERN, line)
    redict = reg.groupdict()
    redict['min'] = int(redict['min'])
    redict['max'] = int(redict['max'])
    return redict


def letter_count(password):
    return Counter(list(password))


def passes_policy(pass_dict, new_policy=False):
    if new_policy:
        # If it's the new policy then extract the letters we are 
        # interested in and set the min/max to 1
        pass_dict['password'] = (pass_dict['password'][pass_dict['min']-1] + 
                                pass_dict['password'][pass_dict['max']-1])
        pass_dict['min'] = 1
        pass_dict['max'] = 1

    letters = letter_count(pass_dict['password'])
    lcount = letters.get(pass_dict['letter'], 0)
    return (lcount >= pass_dict['min'] and
            lcount <= pass_dict['max'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate expenses for Advent of code.')
    parser.add_argument('inputfile', type=str,
                        help='path to list of expenses')
    parser.add_argument('--new-policy', action='store_true', default=False,
                        help='Apply the password policy in part 2')                    
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        password_list = [parse(line) for line in fh.readlines()]

    check_list = [passes_policy(p, new_policy=args.new_policy) for p in password_list]

    print(f'Number of correct passwords {sum(check_list)}')
    print(f'Number of failing passwords {len(check_list)-sum(check_list)}')
