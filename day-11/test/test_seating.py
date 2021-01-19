import pytest

import context
import seating


initial = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

round1 ="""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

round2 = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""

round3 = """#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"""

round4 = """#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##"""

round5 = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""

short = """#.#
#LL"""

class TestEncoding:
    def test_count_occupied(self):
        assert seating.count_occupied(round5) == 37

    def test_adj_indices(self):
        assert sorted(seating.adj_indices(0, 0, 10,10)) == sorted([(0,1), (1,0), (1,1)])
        assert sorted(seating.adj_indices(0, 1, 10,10)) == sorted([(0,0), (0,2), (1,0), (1,1), (1,2)])
        assert sorted(seating.adj_indices(0,9, 10,10)) == sorted([(0,8), (1,8), (1,9)])
        assert sorted(seating.adj_indices(1,0,10,10)) == sorted([(0,0), (0,1), (1,1), (2,0), (2,1)])
        assert sorted(seating.adj_indices(5,2,10,10)) == sorted([(4,1), (4,2), (4,3), (5,1), (5,3), (6,1), (6,2), (6,3)])
        assert sorted(seating.adj_indices(9,0,10,10)) == sorted([(8,0), (8,1), (9,1)])

    def test_str2arr(self):
        assert seating.str2arr(short) == [['#','.', '#'],['#','L','L']]
    
    def test_arr2str(self):
        assert seating.arr2str([['#','.', '#'],['#','L','L']]) == short

    def test_update(self):
        assert seating.update(initial) == round1
    def test_update1(self):
        assert seating.update(round1) == round2
    def test_update2(self):
        assert seating.update(round2) == round3
    def test_update3(self):
        assert seating.update(round3) == round4
    def test_update4(self):
        assert seating.update(round4) == round5
    def test_update5(self):
        assert seating.update(round5) == round5
    def test_play(self):
        assert seating.play(initial) == round5