import pytest

import context
import joltage


testdata = """16
10
15
5
1
11
7
19
6
12
4"""

longer_test_data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


class TestEncoding:
    def test_valid_adapters(self):
        assert joltage.valid_list(0) == set([1, 2, 3])
        assert joltage.valid_list(2) == set([3, 4, 5])

    def test_find_valid(self):
        assert joltage.find_valid(0, [3, 4, 5, 6, 7], min) == 3
        assert joltage.find_valid(6, [3, 4, 5, 6, 7], min) == 7
        assert joltage.find_valid(3, [3, 4, 5, 6, 7], min) == 4
        assert joltage.find_valid(3, [3, 4, 5, 6, 7], max) == 6

    def test_parse(self):
        assert joltage.parse(testdata) == [
                             16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    def test_get_jolts(self):
        adapts = joltage.parse(testdata)
        assert joltage.get_jolts(0, adapts) == {1: 7, 2: 0, 3: 5}

    def test_get_jolts_longer(self):
        adapts = joltage.parse(longer_test_data)
        assert joltage.get_jolts(0, adapts) == {1: 22, 2: 0, 3: 10}

    def test_possible_arrangements(self):
        adapts = joltage.parse(testdata)
        assert joltage.possible_arrangements(adapts) == 8

    def test_n_ways(self):
        counts = {1: 1, 4: 1, 5: 1}
        assert joltage.n_ways(6, {4, 5}, counts) == {1: 1, 4: 1, 5: 1, 6:2}

        counts = {1: 1, 4: 1, 5: 1, 6:2}
        assert joltage.n_ways(7, {4, 5, 6}, counts) == {1: 1, 4: 1, 5: 1, 6:2, 7:4}

        counts = {1: 1, 4: 1, 5: 1, 6:2, 7:4}
        assert joltage.n_ways(10, {7}, counts) == {1: 1, 4: 1, 5: 1, 6:2, 7:4, 10:4}

        counts = {1: 1, 4: 1, 5: 1, 6:2, 7:4, 10:4, 11:4}
        assert joltage.n_ways(12, {10, 11}, counts) == {1: 1, 4: 1, 5: 1, 6:2, 7:4, 10:4, 11:4, 12:8}

    def test_possible_arrangements_longer(self):
        adapts = joltage.parse(longer_test_data)
        assert joltage.possible_arrangements(adapts) == 19208
