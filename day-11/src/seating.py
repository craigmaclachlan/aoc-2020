#!/usr/bin/env python3
import argparse

def count_occupied(plan):
    return plan.count('#')

def adj_indices(y, x, nx, ny):
    return [(dy+y, dx+x) 
            for dx in range(-1,2) for dy in range(-1,2)
            if (dx+x >= 0 and dx+x <= nx-1 and
                dy+y >= 0 and dy+y <= ny-1) and
                (dy,dx) != (0,0)]

def str2arr(text):
    return [list(row) for row in text.split('\n')]

def arr2str(grid):
    return "\n".join(''.join(row) for row in grid)

def update(text):
    grid = str2arr(text)
    output = []
    for iy, row in enumerate(grid):
        out_row = []
        for ix, _ in enumerate(row):
            if grid[iy][ix] == '.': 
                out_row.append('.')
                continue
            indices = adj_indices(iy,ix, len(row), len(grid))
            n_occ = [grid[jy][jx] for jy,jx in indices].count('#')
            if n_occ == 0:
                out_row.append( '#')
            elif n_occ >= 4:
                out_row.append( 'L')
            else:
                out_row.append(grid[iy][ix])
        output.append(out_row)
    return arr2str(output)

def play(text):
    prev = text
    new = update(text)
    i = 1
    while prev != new:
        prev = new
        new = update(new)
        i+=1
    return new


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = fh.read()

    answer1 = count_occupied(play(data))
    print(f'answer 1 = {answer1}')