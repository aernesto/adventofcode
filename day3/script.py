# -*- coding: utf-8 -*-


def mas_frequent(number, total):
    if (total / 2) > number:
        return 0
    return 1


def to_decimal(b):
    agg = 0
    for i, value in enumerate(reversed(b)):
        agg += 2**i if value else 0
    return agg


LENGTH = 12
if __name__ == "__main__":
    import sys
    array = [0] * LENGTH
    with open(sys.argv[1], 'rt') as fh:
        for line_count, line in enumerate(fh):
            for index, character in enumerate(line.strip()):
                digit = int(character)
                if digit:
                    array[index] += 1
    line_count += 1
    gamma = [mas_frequent(x, line_count) for x in array]
    epsilon = [1 - g for g in gamma]
    dg = to_decimal(gamma)
    de = to_decimal(epsilon)
    print(dg * de)
