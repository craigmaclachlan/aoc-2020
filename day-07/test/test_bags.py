import pytest

import context
import bags

testdata = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag."""

test_data_full = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_data_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

class TestBags:
    def test_parse_line(self):
        assert bags.parse_line(
            'light red bags contain 1 bright white bag, 2 muted yellow bags.'
            ) == ('light red', {'bright white': 1, 'muted yellow': 2})
        assert bags.parse_line('faded blue bags contain no other bags.') == ('faded blue', {})

    def test_bag_count(self):
        assert bags.bag_count('1 shiny gold bag') == ('shiny gold', 1)
        assert bags.bag_count('2 vibrant plum bags.') == ('vibrant plum', 2)

    def test_rule_list(self):
        assert bags.rule_list(testdata) == {
            'light red': {'bright white': 1, 'muted yellow': 2},
            'dark orange': {'bright white': 3 , 'muted yellow':4 },
            'bright white': {'shiny gold':1}
            }
        

    def test_could_contain(self):
        rule_list = bags.rule_list(test_data_full)
        assert bags.could_contain(rule_list, 'shiny gold') == set(['bright white', 'muted yellow', 'dark orange', 'light red'])
        assert len(bags.could_contain(rule_list, 'shiny gold')) == 4

    def test_count_contain(self):
        rule_list = bags.rule_list(test_data_2)
        assert bags.count_bags(rule_list, 'shiny gold') == 126

        rule_list = bags.rule_list(test_data_full)
        assert bags.count_bags(rule_list, 'shiny gold') == 32
