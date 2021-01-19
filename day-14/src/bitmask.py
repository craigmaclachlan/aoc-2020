#!/usr/bin/env python3
import argparse
import re
import itertools

def parse_mask(line):
    if line.startswith('mask = '):
        return line.split('=')[1].strip()
    else:
        raise TypeError

mem_pattern = r'mem\[(\d+)\] = (\d+)'
def parse_mem(line):
    retext = re.search(mem_pattern, line)
    return (int(retext.group(1)), int(retext.group(2)))


def int2bytes(num):
    return f'{num:036b}'


def bytes2int(bstring):
    return sum([int(bval) * 2**n for bval, n in zip(list(bstring), range(35, -1, -1))])


def apply_mask(mask, num):
    bnum = int2bytes(num)
    bstr = ''.join([m if m in ['0','1'] else b for m, b in zip(list(mask), list(bnum))])
    return bytes2int(bstr)


def apply_mask_floating(mask, num):
    output = []
    bnum = int2bytes(num)
    bstr = ''.join([m if m in ['X','1'] else b for m, b in zip(list(mask), list(bnum))])

    num_floating = bstr.count('X')
    combinations = itertools.product(['0','1'], repeat=num_floating)
    for comb in combinations:
        tmp_bstr = bstr
        for digit in comb:
            tmp_bstr = tmp_bstr.replace('X', digit, 1)
        output.append(tmp_bstr)
    return [bytes2int(out) for out in output]


def apply_instructs(lines, floating=False):
    mask = ''
    memory = {}
    while len(lines) > 0:
        line = lines.pop(0)
        try:
            mask = parse_mask(line)
            continue
        except TypeError:
            mloc, value = parse_mem(line)

        if floating:
            mlocs = apply_mask_floating(mask, mloc)
            for ml in mlocs:
                memory[ml] = value
        else:
            new_val = apply_mask(mask, value)
            memory[mloc] = apply_mask(mask, new_val)
    return sum(memory.values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = fh.readlines()

    answer1 = apply_instructs(data.copy())
    print('Answer 1 = ', answer1)
    
    answer2 = apply_instructs(data.copy(), floating=True)
    print('Answer 2 = ', answer2)
