import pytest

import context
import bitmask


testdata = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

testdata2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

class TestBitmask:
    def test_parse_mask(self):
        lines = testdata.split('\n')
        assert bitmask.parse_mask(lines[0]) == 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        with pytest.raises(TypeError):
            bitmask.parse_mask(lines[1])
    
    def test_parse_mem(self):
        lines = testdata.split('\n')
        assert bitmask.parse_mem(lines[1]) == (8, 11)
        assert bitmask.parse_mem(lines[2]) == (7, 101)
        assert bitmask.parse_mem(lines[3]) == (8, 0)

    def test_int2bytes(self):
        assert bitmask.int2bytes(11) == '000000000000000000000000000000001011'
        assert bitmask.int2bytes(101) == '000000000000000000000000000001100101'
        assert bitmask.int2bytes(0) == '000000000000000000000000000000000000'

    def test_bytes2int(self):
        assert bitmask.bytes2int('000000000000000000000000000000001011') == 11
        assert bitmask.bytes2int('000000000000000000000000000001100101') == 101
        assert bitmask.bytes2int('000000000000000000000000000000000000') == 0

    def test_mask(self):
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        assert bitmask.apply_mask(mask, 11) == 73
        assert bitmask.apply_mask(mask, 101) == 101
        assert bitmask.apply_mask(mask, 0) == 64

    def test_do_stuff(self):
        lines = testdata.split('\n')
        assert bitmask.apply_instructs(lines) == 165

class TestPartTwo:
    def test_apply_floating(self):
        assert bitmask.apply_mask_floating('000000000000000000000000000000X1001X', 42) == [26,27,58,59]
        assert bitmask.apply_mask_floating('00000000000000000000000000000000X0XX', 26) == [16,17,18,19,24,25,26,27]

    def test_do_stuff2(self):
        lines = testdata2.split('\n')
        assert bitmask.apply_instructs(lines, floating=True) == 208