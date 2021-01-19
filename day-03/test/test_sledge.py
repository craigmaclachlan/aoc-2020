import pytest

import context
import sledge

pattern = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"]

class TestTreeCount:
    def test_correct_tree_count(self):
        assert sledge.tree_count(pattern, 3, 1) == 7

class TestMultiPath:
    def test_multi_path_trees(self):
        assert sledge.tree_count(pattern, 1, 1) == 2
        assert sledge.tree_count(pattern, 3, 1) == 7
        assert sledge.tree_count(pattern, 5, 1) == 3
        assert sledge.tree_count(pattern, 7, 1) == 4
        assert sledge.tree_count(pattern, 1, 2) == 2


class TestGetCoords:
    def test_correct_coords(self):
        x = 2
        y = 1
        rows = 5
        width = 4
        assert sledge.get_coords(x, y, rows, width) == [(0,0), (1,2), (2, 0), (3,2), (4,0)]