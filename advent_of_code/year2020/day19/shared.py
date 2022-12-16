import re


def parse_text(text):
    data = text.split("\n\n")
    rules = data[0].splitlines()
    messages = data[1].splitlines()
    line_pat = re.compile(r'(\d+): (.*)')
    processed_rules = dict()
    for line in rules:
        m = line_pat.match(line)
        processed_rules[m.group(1)] = [k.split() for k in m.group(2).strip('"').split('|')]
    return processed_rules, messages


def build_regex(rules, index='0'):
    mega = dict()

    def func(rules, n):
        pattern = ''
        for i in rules[n]:
            patt = ''
            for j in i:
                if j.isdigit() and j in mega:
                    patt += mega[j]
                elif j.isalpha():
                    mega[n] = j
                    patt += j
                elif j == '+':
                    patt += '+'
                else:
                    patt += func(rules, j)
            pattern += '(' + patt + ')|'
        mega[n] = '(' + pattern.strip('|') + ')'
        return mega[n]

    return re.compile(func(rules, index))
