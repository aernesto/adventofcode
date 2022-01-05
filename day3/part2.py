# -*- coding: utf-8 -*-
def extract_max(llist, bit_number, o2=True):
    total = len(llist)
    ones = [n for n in llist if n[bit_number]]
    zeros = [n for n in llist if not n[bit_number]]
    num_ones, num_zeros = len(ones), len(zeros)
    if o2:
        if num_ones >= num_zeros:
            return ones
        if num_ones < num_zeros:
            return zeros
    else:
        if num_ones < num_zeros:
            return ones
        if num_ones >= num_zeros:
            return zeros


def to_decimal(b):
    agg = 0
    for i, value in enumerate(reversed(b)):
        agg += 2**i if value else 0
    return agg


LENGTH = 12  # number of bits in single number

if __name__ == "__main__":
    import sys
    numbers = []

    # read full list of binary numbers as a list of lists
    with open(sys.argv[1], 'rt') as fh:
        for line_count, line in enumerate(fh):
            bits = []
            for character in line.strip():
                digit = int(character)
                bits.append(digit)
            numbers.append(bits)

    co2_returned = numbers
    current_bit = -1
    #  print("STARTING CO2")
    while len(co2_returned) > 1:
        current_bit += 1
        co2_returned = extract_max(co2_returned, current_bit, False)
        #  print(co2_returned)
    co2 = to_decimal(co2_returned[0])
    print()
    #  print("STARTING O2")
    o2_returned = numbers
    current_bit = -1
    while len(o2_returned) > 1:
        current_bit += 1
        o2_returned = extract_max(o2_returned, current_bit, True)
        #  print(o2_returned)
    o2 = to_decimal(o2_returned[0])

    print(o2, co2)
