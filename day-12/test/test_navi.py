import pytest

import context
import navi


testdata = """F10
N3
F7
R90
F11"""


class TestEncoding:
    def test_move(self):
        ship = navi.Ship('E', 0, 0)
        ship.move('F10')
        assert ship.position() == ('E', -10, 0)
        ship.move('N3')
        assert ship.position() == ('E', -10, 3)
        ship.move('F7')
        assert ship.position() == ('E', -17, 3)
        ship.move('R90')
        assert ship.position() == ('S', -17, 3)
        ship.move('F11')
        assert ship.position() == ('S', -17, -8)

    def test_mdist(self):
        ship = navi.Ship('E', 0, 0)
        ship.move('F10')
        ship.move('N3')
        ship.move('F7')
        ship.move('R90')
        ship.move('F11')

        assert ship.mdist() == 25

    def test_update_heading(self):
        assert navi.update_heading('N', 'R90') == 'E'
        assert navi.update_heading('N', 'R180') == 'S'
        assert navi.update_heading('E', 'L180') == 'W'
        assert navi.update_heading('E', 'R180') == 'W'

    def test_go(self):
        ilist = testdata.split('\n')
        ship = navi.Ship('E', 0, 0)
        ship.go(ilist)
        assert ship.position() == ('S', -17, -8)
        assert ship.mdist() == 25

class TestWaypoint:
    def test_move(self):
        wp = navi.Waypoint(-10, 1, 0, 0)
        wp.move('F10')
        assert wp.position() == (-100, 10)

        wp.move('N3')
        assert wp.wp_position() == (-10, 4)
        assert wp.position() == (-100, 10)

        wp.move('F7')
        assert wp.position() == (-170, 38)

        wp.move('R90')
        assert wp.wp_position() == ( -4, -10)

        wp.move('F11')
        assert wp.position() == (-214, -72)

        assert wp.mdist() == 286