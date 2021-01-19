#!/usr/bin/env python3.8
import argparse
import re

def next_index(current, text):
    retext = re.search(r'jmp ([+-]\d+)', text)
    if retext:
        return current + int(retext.group(1))
    else:
        return current + 1

def accumulator(current, text):
    retext = re.search(r'acc ([+-]\d+)', text)
    if retext:
        return current + int(retext.group(1))
    else:
        return current

def loop(instructions):
    # instructions = text.split('\n')
    used_indices = []
    index = 0
    total = 0
    while index not in used_indices and index < len(instructions):
        used_indices.append(index)
        total = accumulator(total, instructions[index])
        index = next_index(index, instructions[index])
    
    return total, index >= len(instructions)

def invert(line):
    if 'nop' in line:
        return line.replace('nop', 'jmp')
    elif 'jmp' in line:
        return line.replace('jmp', 'nop')
    else:
        raise ValueError


def best_loop(instructions):
    for ind, line in enumerate(instructions):
        if 'nop' in line or 'jmp' in line:
            instructions_copy = instructions.copy()
            instructions_copy[ind] = invert(instructions_copy[ind])
            total, the_best = loop(instructions_copy)
            if the_best:
                break
    return total

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = fh.readlines()

    answer, _ = loop(data)
    print(f'Answer is {answer}')

    best_answer = best_loop(data)
    print(f'best answer is {best_answer}')