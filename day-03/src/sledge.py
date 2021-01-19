#!/usr/bin/env python3.8
import argparse

def tree_count(pattern, dx, dy):
    return sum([ 1 if pattern[row][col] == '#' else 0
    for row, col in get_coords(dx, dy, len(pattern), len(pattern[0]))])

def get_coords(dx, dy, rows, width):
    ys = range(0, rows, dy)
    xs = [dx*n % width for n in range(len(ys))]
    return list(zip(ys, xs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate trees in sledging path')
    parser.add_argument('inputfile', type=str,
                        help='path to list of expenses')
    args = parser.parse_args()
    
    with open(args.inputfile, 'r') as fh:
        inputdata = [line.strip() for line in fh.readlines()]

    num_trees = tree_count(inputdata, 3, 1)

    print(f'Number of trees in first path = {num_trees}')

    num_trees = ( tree_count(inputdata, 1, 1) *
                tree_count(inputdata, 3, 1) *
                tree_count(inputdata, 5, 1) *
                tree_count(inputdata, 7, 1) *
                tree_count(inputdata, 1, 2))

    print(f'Product of Number of trees in alt paths = {num_trees}')