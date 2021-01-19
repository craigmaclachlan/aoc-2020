# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
import re


def byr(passport):
    value = int(passport.get('byr', '0'))
    return value >= 1920 and value <= 2002

def iyr(passport):
    value = int(passport.get('iyr', '0'))
    return value >= 2010 and value <= 2020

def eyr(passport):
    value = int(passport.get('eyr', '0'))
    return value >= 2020 and value <= 2030

def hgt(passport):
    value = passport.get('hgt', 'zz')
    retxt = re.search(r'(\d+)([ci][mn])', value)
    if retxt:
        value = int(retxt.group(1))
        unit = retxt.group(2)
        if unit == 'cm':
            return value >= 150 and value <= 193
        elif unit == 'in':
            return value >= 59 and value <= 76
    return False

def hcl(passport):
    value = passport.get('hcl', 'zz')
    return re.match('#[0-9a-f]{6}', value) is not None

def ecl(passport):
    value = passport.get('ecl', 'zz')
    return value in 'amb blu brn gry grn hzl oth'.split()

def pid(passport):
    value = passport.get('pid', 'zz')
    return re.match('^[0-9]{9}$', value) is not None

checks = [byr, iyr, eyr, hgt, hcl, ecl, pid]

def apply_all(passport):
    return False not in [check(passport) for check in checks]