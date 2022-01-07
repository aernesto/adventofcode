# -*- coding: utf-8 -*-
from collections import Counter

DIGITS = {  # length: digit
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def main_f(fname):
    counter = Counter([])
    with open(fname, 'rt') as fh:
        for line in fh:
            last_part = line.split(' | ')[1]
            four_digits = last_part.split()[:4]
            int_digits = [
                DIGITS[len(string)] for string in four_digits
                if (len(string) in DIGITS)
            ]
            counter.update(int_digits)
    return counter.total()


if __name__ == "__main__":
    import sys
    print(main_f(sys.argv[1]))
