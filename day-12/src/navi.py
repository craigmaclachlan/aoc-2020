#!/usr/bin/env python3
import argparse

points = ['N', 'E', 'S', 'W']
angle = [0, 90, 180, 270]
compass = dict(zip(points, angle))
ssapmoc = dict(zip(angle, points))

def update_heading(current, update):
    angle = compass[current]
    dang = int(update.replace('R', '+').replace('L', '-'))
    return ssapmoc[(angle+dang)%360]

def rotate_wp(ns, ew, update):
    """Yuk"""
    if update == 'R90' or update == 'L270':
        return (ew, -ns)
    elif update == 'R180' or update == 'L180':
        return (-ns, -ew)
    elif update == 'R270' or update == 'L90':
        return (-ew, ns)
    print('|',update,'|')

class Ship(object):
    def __init__(self, heading, ns, ew):
        self.heading = heading
        self.ns = ns
        self.ew = ew
    
    def move(self, instruction):
        if instruction.startswith('F'):
            instruction = instruction.replace('F', self.heading)
        if instruction.startswith('R') or instruction.startswith('L'):
            self.heading = update_heading(self.heading, instruction)
        if instruction.startswith('N') or instruction.startswith('S'):
            self.ns += int(instruction.replace('N', '+').replace('S', '-'))
        if instruction.startswith('E') or instruction.startswith('W'):
            self.ew += int(instruction.replace('W', '+').replace('E', '-'))

    def position(self):
        return (self.heading, self.ew, self.ns)

    def mdist(self):
        return abs(self.ns) + abs(self.ew)

    def go(self, ilist):
        for ins in ilist:
            self.move(ins)

class Waypoint(Ship):
    def __init__(self, wp_ew, wp_ns, sh_ew, sh_ns):
        self.wp_ew = wp_ew
        self.wp_ns = wp_ns
        self.ew = sh_ew
        self.ns = sh_ns

    def move(self, instruction):
        if instruction.startswith('F'):
            value = int(instruction.replace('F', ''))
            self.ew += value * self.wp_ew
            self.ns += value * self.wp_ns
        if instruction.startswith('R') or instruction.startswith('L'):
            self.wp_ns, self.wp_ew = rotate_wp(self.wp_ns, self.wp_ew, instruction)
        if instruction.startswith('N') or instruction.startswith('S'):
            self.wp_ns += int(instruction.replace('N', '+').replace('S', '-'))
        if instruction.startswith('E') or instruction.startswith('W'):
            self.wp_ew += int(instruction.replace('W', '+').replace('E', '-'))
    
    def position(self):
        return (self.ew, self.ns)
    
    def wp_position(self):
        return (self.wp_ew, self.wp_ns)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('inputfile', type=str,
                        help='path to input data')
    args = parser.parse_args()

    with open(args.inputfile, 'r') as fh:
        data = [s.strip() for s in fh.readlines()]

    ship = Ship('E', 0, 0)
    ship.go(data)
    print(f'M dist = {ship.mdist()}')
    
    wp = Waypoint(-10, 1, 0, 0)
    wp.go(data)
    print(f'M dist (waypoints) = {wp.mdist()}')