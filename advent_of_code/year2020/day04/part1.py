import re


def main(text: str) -> int:
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    data = text.split('\n\n')
    count = 0
    for row in data:
        if required.issubset(set(re.findall(r'(\S*?):', row))):
            count += 1
    return count
