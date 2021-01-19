import pytest

import context
import ticket


testdata = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

class TestBitmask:
    def test_parse_rule(self):
        assert ticket.parse_rule('class: 1-3 or 5-7') == ('class', [1,2,3,5,6,7])
        assert ticket.parse_rule('row: 6-11 or 33-44') == ('row', list(range(6,12))+list(range(33,45)))
        assert ticket.parse_rule('seat: 13-40 or 45-50') == ('seat', list(range(13,41))+list(range(45,51)))
        assert ticket.parse_rule('arrival track: 13-40 or 45-50') == ('arrival track', list(range(13,41))+list(range(45,51)))

    def test_get_rules(self):
        assert ticket.get_rules(testdata) == {
            'class': [1,2,3,5,6,7],
            'row': list(range(6,12))+list(range(33,45)),
            'seat': list(range(13,41))+list(range(45,51))
        }

    def test_parse_your_ticket(self):
        assert ticket.parse_your_ticket(testdata) == [7,1,14]

    def test_parse_nearby_tickets(self):
        assert ticket.parse_nearby_tickets(testdata) == [
            [7,3,47],
            [40,4,50],
            [55,2,20],
            [38,6,12]]
    
    def test_invalid_fields(self):
        rules = ticket.get_rules(testdata)
        assert ticket.invalid_fields(rules, [7,3,47]) == 0
        assert ticket.invalid_fields(rules, [40,4,50]) == 4
        assert ticket.invalid_fields(rules, [55,2,20]) == 55
        assert ticket.invalid_fields(rules, [38,6,12]) == 12

    def test_scan_all_tickets(self):
        assert ticket.scan_all_tickets(testdata) == 71