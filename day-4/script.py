import re

with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')
    passports = [re.split(' |\n', passport) for passport in passports]
    passports = [{p.split(':')[0]: p.split(':')[1] for p in passport if p != ''} for passport in passports]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_count_a = 0

for passport in passports:
    if required.issubset(set(passport.keys())):
        valid_count_a += 1

print(valid_count_a)


# Part B


def check_field(key, value):

    if key == 'byr' and value.isdigit():
        return 1920 <= int(value) <= 2002
    elif key == 'iyr' and value.isdigit():
        return 2010 <= int(value) <= 2020
    elif key == 'eyr' and value.isdigit():
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if 'cm' in value:
            height = int(value.replace('cm', '')) if value.replace('cm', '').isdigit() else 0
            return 150 <= height <= 193
        elif 'in' in value:
            height = int(value.replace('in', '')) if value.replace('in', '').isdigit() else 0
            return 59 <= height <= 76
    elif key == 'hcl':
        return re.match('#[0-9a-f]{6}$', value)
    elif key == 'ecl':
        return re.match('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', value)
    elif key == 'pid':
        return re.match('^[0-9]{9}$', value)
    elif key == 'cid':
        return True
    return False


# thanks @aelred


def check_validity(passport):

    if not required.issubset(set(passport.keys())):
        return False
    for key, value in passport.items():
        if not check_field(key, value):
            return False
    return True


def count_valid_passports():

    valid_count_b = 0
    for p in passports:
        if check_validity(p):
            valid_count_b += 1
    return valid_count_b


print(count_valid_passports())
