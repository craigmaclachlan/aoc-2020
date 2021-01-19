import pytest

import context
import counting


class TestCounting:
    def test_play(self):
        assert counting.play([0,3,6]) == 436
        assert counting.play([1,3,2]) == 1
        assert counting.play([2,1,3]) == 10
        assert counting.play([1,2,3]) == 27
        assert counting.play([2,3,1]) == 78
        assert counting.play([3,2,1]) == 438
        assert counting.play([3,1,2]) == 1836

    def test_play_long(self):
        assert counting.play([0,3,6], nrounds=30000000) == 175594
    
    # def test_play_long2(self):
    #     assert counting.play([1,3,2], nrounds=30000000) == 2578
    # def test_play_long3(self):
    #     assert counting.play([2,1,3], nrounds=30000000) == 3544142
        # assert counting.play([1,2,3], nrounds=30000000) == 261214
        # assert counting.play([2,3,1], nrounds=30000000) == 6895259
        # assert counting.play([3,2,1], nrounds=30000000) == 18
        # assert counting.play([3,1,2], nrounds=30000000) == 362
