import pytest

import context
import boarding


class TestFinder:
    def test_finder(self):
        assert boarding.finder('FBFBBFF') == 44
        assert boarding.finder('RLR') == 5

    def test_seat_id(self):
        assert boarding.seat_id('FBFBBFFRLR') == 357
        assert boarding.seat_id('BFFFBBFRRR') == 567
        assert boarding.seat_id('FFFBBBFRRR') == 119
        assert boarding.seat_id('BBFFBBFRLL') == 820