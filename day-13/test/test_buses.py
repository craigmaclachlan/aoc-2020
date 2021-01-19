import pytest

import context
import buses


testdata = """939
7,13,x,x,59,x,31,19"""


class TestBuses:
    def test_time_to_next(self):
        assert buses.ttn(939, 59) == 5
        assert buses.ttn(939, 7) == 6
        assert buses.ttn(939, 13) == 10

    def test_parse(self):
        assert buses.parse(testdata) == (939, [7,13,'x', 'x',59,'x',31,19])

    def test_find_next(self):
        t, b = buses.parse(testdata)
        assert buses.find_next(t,b) == 295

    def test_synchro_bus(self):
        _, b = buses.parse(testdata)
        assert buses.synchro_bus(b) == 1068781
        assert buses.synchro_bus([17,'x',13,19]) == 3417
        assert buses.synchro_bus([67,7,59,61]) == 754018
        assert buses.synchro_bus([1789,37,47,1889]) == 1202161486

