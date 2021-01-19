#!/usr/bin/env python3.8
import argparse
import re
from itertools import chain


def bag_count(text):
    retext = re.search(r'(\d+) ([a-z ]+) bag', text)
    return retext.group(2), int(retext.group(1))


def parse_line(text):
    part1, part2 = text.split('contain')
    part1 = part1.replace(' bags ', '')
    if part2.startswith(' no other'):
        bags_dict = {}
    else:
        bags = part2.split(',')
        bags_list = [bag_count(b) for b in bags]
        bags_dict = {k: v for k, v in bags_list}
    return part1, bags_dict


def rule_list(text):
    return dict([parse_line(rule) for rule in text.split('\n')])


def could_contain(rules, bag):
    directly_contain = [colour for colour, sub_bags in rules.items() if bag in sub_bags]

    indirect_contain = [could_contain(rules, subbag) for subbag in directly_contain]
    if len(indirect_contain) >0:
        directly_contain.extend(list(chain.from_iterable(indirect_contain))) 
    return set(directly_contain)


def count_bags(rules, bag):
    count = 0
    bag_contains = rules[bag]
    for subbag, value in bag_contains.items():
        sub_bag_count = count_bags(rules, subbag)
        count += value + value * sub_bag_count
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Seat finder')
    parser.add_argument('inputfile', type=str,
                        help='path to list of customs form answers')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = fh.read()

    rules = rule_list(data)

    contain_gold = could_contain(rules, 'shiny gold')

    print(f'Number of bags to contain shiny gold one = {len(contain_gold)}')

    count = count_bags(rules, 'shiny gold')
    print(f'the second part = {count}')