#!/usr/bin/env python3
import argparse
from collections import defaultdict
from functools import reduce

class Hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self))

def valid_list(jolts):
    return set([jolts+1, jolts+2, jolts+3])

def valid_down(jolts):
    return set([jolts-1, jolts-2, jolts-3])

def find_valid(jolts, available, select):
    return select(set(available) & valid_list(jolts))

def parse(text):
    return [int(line) for line in text.split('\n')]

def n_ways(num, choices, n_ways_hist):
    count = 0
    for val in choices:
        count += n_ways_hist[val]
    n_ways_hist[num] = count
    return n_ways_hist

def possible_arrangements(adapts):
    choices = defaultdict(int)
    tmp_adapts = sorted([0] + adapts.copy(), reverse=True)
    while len(tmp_adapts) > 1:
        item = tmp_adapts.pop(0)
        choices[item] = set(tmp_adapts) & valid_down(item)

    n_ways_hist = {0:1}
    for k in sorted(choices.keys()):
        n_ways_hist = n_ways(k, choices[k], n_ways_hist)
    return max(n_ways_hist.values())


def get_jolts(start, adapts, select_func=min):
    tmp_adapts = sorted(adapts.copy())
    diffs = [b-a for a, b in zip([0]+tmp_adapts, tmp_adapts+[tmp_adapts[-1]+3])]
    return {1:diffs.count(1), 2:diffs.count(2), 3:diffs.count(3)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = parse(fh.read())

    answer1 = get_jolts(0, data)
    print('Answer 1 = ', answer1[1]*answer1[3])

    answer2 = possible_arrangements(data)
    print('Answer 2 = ', answer2)
