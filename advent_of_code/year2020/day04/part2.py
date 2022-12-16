import re


def main(text: str) -> int:
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    data = text.split('\n\n')
    count = 0
    for row in data:
        d = dict(re.findall(r'(\S*?):(\S*)', row))
        if all(k in d for k in required):
            try:
                assert 1920 <= int(d['byr']) <= 2002
                assert 2010 <= int(d['iyr']) <= 2020
                assert 2020 <= int(d['eyr']) <= 2030
                assert d['hgt'].endswith('cm') or d['hgt'].endswith('in')
                if d['hgt'].endswith('cm'):
                    assert 150 <= int(d['hgt'][:-2]) <= 193
                if d['hgt'].endswith('in'):
                    assert 59 <= int(d['hgt'][:-2]) <= 76
                assert re.fullmatch(r'#[0-9A-Fa-f]{6}', d['hcl'])
                assert d['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                assert re.fullmatch(r'\d{9}', d['pid'])
                count += 1
            except AssertionError:
                pass
    return count
