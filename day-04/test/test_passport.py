import pytest

import context
import passport
import checks

inputdata = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


class TestParseInput:
    def test_parse_input(self):
        data = passport.parse_input(inputdata)
        assert data[0] == {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
                           'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
        assert data[1] == {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                           'hcl': '#cfa07d', 'byr': '1929'}


class TestCheckReqFields:
    def test_req_fields_valid(self):
        inputdata = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
                     'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}

        assert passport.check_fields(
            inputdata, 'byr iyr eyr hgt hcl ecl pid'.split()) == True

    def test_req_fields_invalid(self):
        inputdata = {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                     'hcl': '#cfa07d', 'byr': '1929'}

        assert passport.check_fields(
            inputdata, 'byr iyr eyr hgt hcl ecl pid'.split()) == False

    def test_req_fields_invalid2(self):
        inputdata = {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                     'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}

        assert passport.check_fields(
            inputdata, 'byr iyr eyr hgt hcl ecl pid'.split()) == False

    def test_check_all(self):
        data = passport.parse_input(inputdata)
        print(data)

        assert passport.check_all(data, 'byr iyr eyr hgt hcl ecl pid'.split()) == [
            True, False, True, False]

inputdata_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

inputdata_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

class TestHardChecks:
    def test_all_invalid(self):
        passports = passport.parse_input(inputdata_invalid)
        assert sum(passport.check_all(passports, '', hard=True)) == 0
    
    def test_all_valid(self):
        passports = passport.parse_input(inputdata_valid)
        assert sum(passport.check_all(passports, '', hard=True)) == 4

    def test_byr(self):
        assert checks.byr({'byr': '2002'}) == True
        assert checks.byr({'byr': '2003'}) == False

    def test_hgt(self):
        assert checks.hgt({'hgt': '60in'}) == True
        assert checks.hgt({'hgt': '190cm'}) == True
        assert checks.hgt({'hgt': '190in'}) == False
        assert checks.hgt({'hgt': '190'}) == False

    def test_hcl(self):
        assert checks.hcl({'hcl': '#123abc'}) == True
        assert checks.hcl({'hcl': '#123abz'}) == False
        assert checks.hcl({'hcl': '123abc'}) == False

    def test_ecl(self):
        assert checks.ecl({'ecl': 'brn'}) == True
        assert checks.ecl({'ecl': 'wat'}) == False

    def test_pid(self):
        assert checks.pid({'pid': '000000001'}) == True
        assert checks.pid({'pid': '0123456789'}) == False
