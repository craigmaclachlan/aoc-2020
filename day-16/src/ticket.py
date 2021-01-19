#!/usr/bin/env python3
import argparse
import re
import itertools
from collections import defaultdict
from functools import reduce

rule_patten = r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)'
def parse_rule(line):
    retext = re.search(rule_patten, line)
    x1 = int(retext.group(2))
    x2 = int(retext.group(3))
    y1 = int(retext.group(4))
    y2 = int(retext.group(5))
    return (retext.group(1), list(range(x1,x2+1))+list(range(y1,y2+1)))


def get_rules(blob):
    rules_text = blob.split('\n\n')[0].split('\n')
    return dict([parse_rule(line) for line in rules_text])


your_ticket_pattern = r'your ticket:\n([\d,]+)'
def parse_your_ticket(blob):
    retext = re.search(your_ticket_pattern, blob)
    return [int(v) for v in retext.group(1).split(',')]


def parse_nearby_tickets(blob):
    numbers_text = blob.split(':')[-1].strip()
    return [list(map(int, line.split(','))) for line in numbers_text.split('\n')]


def invalid_fields(rules, ticket):
    output = [0]
    for number in ticket:
        is_valid = False
        tmp_output = 0
        for _, valid_nums in rules.items():
            if number in valid_nums:
                is_valid = True
            else:
                tmp_output = number
        if not is_valid:
            output.append(tmp_output)
    return sum(output)


def find_rules_order(rules, tickets):
    ordered_rules = defaultdict(list)

    for i in range(len(tickets[0])):
        all_ith = [t[i] for t in tickets]
        for fname, valid_nums in rules.items():
            number_tickets_passing = len([val for val in all_ith if val in valid_nums])
            if number_tickets_passing == len(all_ith):
                ordered_rules[i].append(fname)
                # break

    return ordered_rules

def scan_all_tickets(blob):
    rules = get_rules(blob)
    tickets = parse_nearby_tickets(blob)
    return sum([invalid_fields(rules, t) for t in tickets])


def is_unique(rules_order):
    for k, v in rules_order.items():
        if len(v) > 1:
            return False
    return True


def find_singular(rules_order, ignore):
    for k, v in rules_order.items():
        if len(v) == 1 and v[0] not in ignore:
            return k, v[0]
    raise ValueError('No singular fields')


def reduce_rules_order(rules_order):
    i=0
    ignore = []
    while not is_unique(rules_order) and i< 100:
        i+=1
        ind, field_name = find_singular(rules_order, ignore)
        ignore.append(field_name)
        for k, v in rules_order.items():
            if k != ind and field_name in v:
                v.remove(field_name)

    return rules_order


def find_order(blob):
    rules = get_rules(blob)
    tickets = parse_nearby_tickets(blob)
    my_ticket = parse_your_ticket(blob)
    valid_tickets = [t for t in tickets if invalid_fields(rules, t) == 0]

    rules_order = find_rules_order(rules, valid_tickets)
    uniq_rules_order = reduce_rules_order(rules_order)

    relevant_inds = [k for k, v in uniq_rules_order.items() if v[0].startswith('departure')] 

    return reduce(lambda x,y: x*y, [my_ticket[i] for i in relevant_inds])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = fh.read()

    
    answer1 = scan_all_tickets(data)
    print('Answer 1 = ', answer1)

    answer2 = find_order(data)
    print('Answer 2 = ', answer2)
    