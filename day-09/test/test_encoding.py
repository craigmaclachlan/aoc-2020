import pytest

import context
import encoding


testdata = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

class TestEncoding:
    def test_is_valid(self):
        data = list(range(1,26))
        assert encoding.is_valid(data+[26]) == True
        assert encoding.is_valid(data+[49]) == True
        assert encoding.is_valid(data+[100]) == False
        assert encoding.is_valid(data+[50]) == False

    def test_window(self):
        array = list(range(1,11))
        expected = [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9], [8,9,10]]
        for item, exp in zip(encoding.window(array, n=3), expected): 
            assert list(item) == exp

    def test_full_example(self):
        data = encoding.parse(testdata)
        assert encoding.check_array(data, 5) == 127

    def test_parse(self):
        assert encoding.parse(testdata) == [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

    def test_find_contiguous_sum(self):
        data = encoding.parse(testdata)
        assert encoding.find_contiguous_sum(data,127) == 62