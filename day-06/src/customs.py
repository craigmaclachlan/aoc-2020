#!/usr/bin/env python3.8
import argparse
from collections import Counter

def count_any(answers):
    return len(set(answers.replace('\n', '')))


def count_matching(answers):
    ans_list = answers.split('\n')
    n_group = len(ans_list)
    counts = Counter(answers.replace('\n', ''))
    return sum([val == n_group for val in counts.values()])


def flatten(blob):
    return [s for s in blob.split("\n\n")]

def count_all(text, matching=False):
    count_fn = count_matching if matching else count_any

    data = flatten(text)
    return [count_fn(item) for item in data]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Seat finder')
    parser.add_argument('inputfile', type=str,
                        help='path to list of customs form answers')
    args = parser.parse_args()
    
    with open(args.inputfile, 'r') as fh:
        data = fh.read()
    
    counts = count_all(data)

    print(f'Sum of the counts = {sum(counts)}')

    counts_m = count_all(data, matching=True)
    print(f'Sum of the matching counts = {sum(counts_m)}')
