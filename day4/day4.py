import re

def get_input():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1

def valid_range(value, start, end):
    return int(value) >= start and int(value) <= end

def valid_height(height):
    m = re.match('^(\d+)(\S\S)$', height)
    if m:
        (start, end) = (150, 193) if m.group(2) == 'cm' else (59, 76)
        return valid_range(m.group(1), start, end)
    else:
        return False

def valid_hair(color):
    return None != re.search('^#[0-9a-f]{6}', color)

def valid_eye(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(pid):
    return None != re.search('^\d{9}$', pid)

def is_valid(passport):
    retval = all(key in passport for key in ['byr',
                                             'iyr',
                                             'eyr',
                                             'hgt',
                                             'hcl',
                                             'ecl',
                                             'pid']) and \
    valid_range(passport['byr'], 1920, 2002) and \
    valid_range(passport['iyr'], 2010, 2020) and \
    valid_range(passport['eyr'], 2020, 2030) and \
    valid_height(passport['hgt']) and \
    valid_hair(passport['hcl']) and \
    valid_eye(passport['ecl']) and \
    valid_pid(passport['pid'])

    return(retval)

entries = get_input()
passports = []
passport = {}
while entries:
    line = entries.pop(0)
    m = re.findall('(\S+):(\S+)', line)
    for (k,v) in m:
        passport[k] = v
    if line == '':
        passports.append(passport)
        passport = {}

passports.append(passport)

count = 0
for passport in passports:
    if is_valid(passport):
        count += 1
print(count)
