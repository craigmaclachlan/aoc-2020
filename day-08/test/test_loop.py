import pytest

import context
import loop

testdata = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class TestLoop:
    def test_next_index(self):
        assert loop.next_index(1, 'acc +7') == 2
        assert loop.next_index(1, 'acc -7') == 2

        assert loop.next_index(2, 'jmp -1') == 1
        assert loop.next_index(1, 'jmp +7') == 8

        assert loop.next_index(1, 'nop +7') == 2
        assert loop.next_index(1, 'nop -1') == 2

    def test_acc(self):
        assert loop.accumulator(1, 'acc +7') == 8
        assert loop.accumulator(1, 'acc -7') == -6

        assert loop.accumulator(2, 'jmp -1') == 2
        assert loop.accumulator(1, 'jmp +7') == 1

        assert loop.accumulator(1, 'nop +7') == 1
        assert loop.accumulator(1, 'nop -1') == 1

    def test_loop(self):
        instructions = testdata.split('\n')
        assert loop.loop(instructions) == ( 5, False )

    def test_find_best_loop(self):
        instructions = testdata.split('\n')
        assert loop.best_loop(instructions) == 8