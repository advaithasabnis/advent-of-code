import re


def sort_string(t):
    return ''.join(sorted(t))


def decrypt(test):
    """Generates the key based on the 10 unique digits in segment-coded form

    Parameters
    ----------
    test : str
        Input string of 10 unique digits in the segment-coded form

    Returns
    -------
    dict
        Dictionary containing the 7-segment digit -> int mapping
    """
    key = dict({8: set('abcdefg')})
    # Sorted so we can decrypt 5 and 6 segment digits
    # Sets because set operations are useful here
    digits = tuple(map(set, sorted(test.split(), key=len)))
    for digit in digits:
        match len(digit):
            # Digits with unique number of segments
            case 2:
                key[1] = digit
            case 3:
                key[7] = digit
            case 4:
                key[4] = digit
            case 5:
                # Segments of 7 are a subset of those of 3
                if key[7] < digit:
                    key[3] = digit
                # Segments in 4 but not in 1 are a subset of those of 5
                elif key[4] - key[1] < digit:
                    key[5] = digit
                # Only other 5 segment digit is 2
                else:
                    key[2] = digit
            case 6:
                # Segments of 4 are a subset of those of 9
                if key[4] < digit:
                    key[9] = digit
                # Segments in 8 but not in 7 are a subset of those of 6
                elif key[8] - key[7] < digit:
                    key[6] = digit
                # Only other 6 segment digit is 0
                else:
                    key[0] = digit

    return {''.join(sorted(v)): str(k) for k, v in key.items()}


def decode_output(output, key):
    """Decodes a 7-segment digit using the given key

    Parameters
    ----------
    output : str
        7-segment digit
    key : dict
        Dictionary containing 7-segment digit to int mapping

    Returns
    -------
    int
        Decoded integer value
    """
    digits = tuple(map(sort_string, output.split()))
    output_value = [key[digit] for digit in digits]
    return int(''.join(output_value))


def main(text):
    pattern = re.compile(r'^([\w\s]+) \| ([\w\s]+)$', re.M)
    output_sum = 0
    for i in pattern.finditer(text):
        test = i.group(1)
        output = i.group(2)
        key = decrypt(test)
        output_sum += decode_output(output, key)
    return output_sum


_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".strip()
assert main(_input) == 61229
