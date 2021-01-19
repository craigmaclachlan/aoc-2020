import pytest

import context
import customs

inputdata = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestCountAnswers:
    def test_count_any(self):
        assert customs.count_any('abc') == 3
        assert customs.count_any('aaaa') == 1

    def test_flatten(self):
        assert customs.flatten(inputdata) == ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']

    def test_count_all(self):
        assert customs.count_all(inputdata) == [3, 3, 3, 1, 1]

    def test_count_matching(self):
        assert customs.count_matching('abc') == 3
        assert customs.count_matching('a\nb\nc') == 0
        assert customs.count_matching('ab\nac') == 1
        assert customs.count_matching('a\na\na\a') == 1
        assert customs.count_matching('b') == 1

    def test_count_all_matching(self):
        assert customs.count_all(inputdata, matching=True) == [3, 0, 1, 1, 1]
        