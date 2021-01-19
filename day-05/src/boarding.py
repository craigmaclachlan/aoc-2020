#!/usr/bin/env python3.8
import argparse
import string
# {'F': '0', 'B':'1', 'L': '0', 'R':'1'}
def finder(location):
    table = location.maketrans('FBLR', '0101')
    location = list(location.translate(table))
    location.reverse()
    number = 0
    for ind, loc in enumerate(location):
        number += 2**ind * int(loc)
    return number

def seat_id(seat_binary, nrow=7):

    row = finder(seat_binary[0:nrow])
    col = finder(seat_binary[nrow:])
    return row*(nrow+1) + col

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Seat finder')
    parser.add_argument('inputfile', type=str,
                        help='path to list of passport details')
    args = parser.parse_args()
    
    with open(args.inputfile, 'r') as fh:
        data = fh.readlines()
    
    seat_ids = [seat_id(seat.strip()) for seat in data]

    print(f"Highest seat index = {max(seat_ids)}")

    expected_seats = set(range(min(seat_ids), max(seat_ids)))
    missing_seats = expected_seats - set(seat_ids)
    print(f'missing seat id = {missing_seats.pop()}')
