#!/usr/bin/env python3.8
import argparse
import re

from collections import deque

def window(seq, n=5):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win


def is_valid(in_array):
    array = in_array.copy()
    target = array.pop()
    options = [target - value for value in array]
    for opt in options:
        if opt in array and 2*opt != target:
            return True
    return False

def parse(text):
    return [int(t) for t in text.split('\n')]

def check_array(array, len_window):
    for windy in window(array, len_window+1):
        sub_array = list(windy)
        if not is_valid(sub_array):
            return sub_array.pop()
    raise ValueError('no problem here')

def find_contiguous_sum(array, target):
    for ind in range(len(array)):
        accum = 0
        jnd = ind
        while accum < target:
            accum += array[jnd]
            jnd+=1
        if accum == target:
            contig_numbers = array[ind:jnd]
            return min(contig_numbers) + max(contig_numbers)
    raise ValueError('not found')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = parse(fh.read())

    first_fail = check_array(data, 25)
    print(f'first fail = {first_fail}')

    answer2 = find_contiguous_sum(data, first_fail)
    print(f'answer 2 = {answer2}')