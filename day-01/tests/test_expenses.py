import pytest

import context
import expenses

class TestExpensesTwoNum:
    def test_perfect_match(self):
        numbers = [167, 2020-811, 334, 811]
        assert expenses.calc_two_nums(numbers) == (2020-811)*811

    def test_example(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        assert expenses.calc_two_nums(numbers) == 514579

    def test_error(self):
        with pytest.raises(IndexError):
            expenses.calc_two_nums([167, 2060, 334, 811])

class TestExpensesThreeNum:
    def test_perfect_match(self):
        numbers = [167, 1000, 1010, 10, 811]
        assert expenses.calc_three_nums(numbers) == 1000 * 1010 * 10

    def test_example(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        assert expenses.calc_three_nums(numbers) == 241861950

    def test_error(self):
        with pytest.raises(IndexError):
            expenses.calc_three_nums([167, 2060, 334, 811])