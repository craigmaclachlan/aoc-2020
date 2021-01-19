#!/usr/bin/env python3
import argparse

def parse(text):
    lines = text.split('\n')
    blist = [item if item == 'x' else int(item) for item in lines[1].split(',')]
    return (int(lines[0]), blist)

def ttn(current, sched):
    return sched - (current % sched)

def find_next(ctime, blist):
    ttbus = [(ttn(ctime, b), b )for b in blist if b != 'x']
    soonest = sorted(ttbus).pop(0)
    return soonest[0] * soonest[1]

def create_check(off, mod):

    def check(n):
        return (n+off) % mod == 0
    
    return check


def synchro_bus(blist):
"""Too slow. Ideal solution involves Chinese Remainder theorem"""

    jnd = float(1)
    ind=0
    steps, offset = max([(b, n) for n, b in enumerate(blist) if b != 'x'])
    funcs = [create_check(n, b) for n, b in enumerate(blist) if b != 'x']
    while ind < 1202161486000:
        jnd += float(1)
        ind = jnd * steps - offset
        
        for func in funcs:
            if not func(ind):
                break
        if func(ind):
            return ind



# x = 0 mod 67 ;  x = 67a
# x = 6 mod 7   ; x = 7b + 6
# x = 57 mod 59 ; x = 59c + 57
# x = 58 mod 61 ; x = 61d + 58 ; 

#  67*a + 61*b = 58
# N = 67*7*59*61

# 67 | 0 | N/67 | 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        ctime, buslist = parse(fh.read())

    answer1 = find_next(ctime, buslist)
    print(f'ID of first bus: {answer1}')

    answer2 = synchro_bus(buslist)
    print(f'time for bus synchro: {answer2}')