#!/usr/bin/env python3
# import argparse

def play(nums, nrounds=2020):
    counter = {k:i+1 for i, k in enumerate(nums)}
    last_number = 0
    for  i in range(len(nums)+1, nrounds):
        last_found = counter.get(last_number)
        if last_found:
            new_number = i - last_found
        else:
            new_number = 0
        counter[last_number] = i
        last_number = new_number
        i += 1

    return last_number


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Play a game')
    # parser.add_argument('inputfile', type=str,
    #                     help='path to input data')
    # args = parser.parse_args()

    # with open(args.inputfile, 'r') as fh:
    #     data = fh.readlines()

    data = [13,16,0,12,15,1]

    answer1 = play(data.copy())
    print('Answer 1 = ', answer1)
    
    answer2 = play(data.copy(), nrounds=30000000)
    print('Answer 2 = ', answer2)

