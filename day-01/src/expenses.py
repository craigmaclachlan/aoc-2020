#!/usr/bin/env python3.8
import argparse

def calc_two_nums(exp_list, target=2020):
    temp_list = exp_list.copy()
    while len(temp_list) > 1:
        first_number = temp_list.pop()
        second_number = target-first_number
        if second_number in temp_list:
            return first_number * second_number

    raise IndexError('Unable to find matching numbers')

def calc_three_nums(exp_list, target=2020):
    while len(exp_list) > 2:
        first_number = exp_list.pop()
        try:
            two_num_product = calc_two_nums(exp_list, target=2020-first_number)
            return first_number * two_num_product
        except IndexError:
            continue
            
    raise IndexError('Unable to find matching numbers')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate expenses for Advent of code.')
    parser.add_argument('inputfile', type=str,
                        help='path to list of expenses')
    parser.add_argument('--three', action='store_true', default=False,
                        help='Find the product of 3 numbers that sum to 2020')
    args = parser.parse_args()
    
    with open(args.inputfile, 'r') as fh:
        inputdata = [int(line) for line in fh.readlines()]

    if args.three:
        answer = calc_three_nums(inputdata)
    else:
        answer = calc_two_nums(inputdata)
    print(f'The answer is: {answer}')