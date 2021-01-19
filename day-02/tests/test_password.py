import pytest

import context
import password

class TestParseData:
    def test_correct_parse(self):
        line = "1-3 a: abcde"
        assert password.parse(line) == {'min':1, 'max':3, 'letter': 'a', 'password': 'abcde'}

class TestCountLetters:
    def test_correct_count(self):
        string = 'abcd'
        assert password.letter_count(string) == {'a':1, 'b':1, 'c':1, 'd':1 }

class TestCheckPolicy:
    def test_passes_policy(self):
        parsed_pass = {'min':1, 'max':3, 'letter': 'a', 'password': 'abcde'}
        assert password.passes_policy(parsed_pass) == True
    
    def test_fails_policy(self):
        parsed_pass = {'min':2, 'max':3, 'letter': 'a', 'password': 'abcde'}
        assert password.passes_policy(parsed_pass) == False

    def test_passes_new_policy(self):
        parsed_pass = {'min':1, 'max':3, 'letter': 'a', 'password': 'abcde'}
        assert password.passes_policy(parsed_pass, new_policy=True) == True
    
    def test_fails_new_policy(self):
        parsed_pass = {'min':1, 'max':3, 'letter': 'b', 'password': 'cdefg'}
        assert password.passes_policy(parsed_pass, new_policy=True) == False
        
    def test_fails_new_policy_again(self):
        parsed_pass = {'min':2, 'max':9, 'letter': 'c', 'password': 'ccccccccc'}
        assert password.passes_policy(parsed_pass, new_policy=True) == False
