# -*- coding: utf-8 -*-
"""module to solve part II of day 8"""
from pprint import pprint
from typing import Sequence


def learn_mapping(ten_strings: Sequence[str]):
    """returns a dict mapping frozenset of strings to int"""

    # the mapping for digits 1, 4, 7, 8 is easy to learn
    _easy = {7: 3, 4: 4, 1: 2, 8: 7}  # maps digit to str len

    def easy_digits(digit):
        """will be used for each 'easy digit'"""
        st = [s for s in ten_strings if len(s) == _easy[digit]][0]
        return frozenset(st)

    # start building the dict returned by the present function
    map_ = {easy_digits(d): d for d in _easy}

    # let's start building a mapping of our 7 segments to the 7 letters
    def extract(fs: frozenset) -> str:
        return next(iter(fs))

    seven, one = easy_digits(7), easy_digits(1)
    seg2letter = {'H': seven - one}  # top horizontal segment

    # next we focus on the mapping for 2, 3, 5
    five_segments = [frozenset(s) for s in ten_strings if len(s) == 5]
    three_horizontal = frozenset.intersection(*five_segments)

    inv_map_ = {v: k for k, v in map_.items()}
    four_vertical = inv_map_[8] - three_horizontal

    # also, intersection, 3, 5, 2, 4, we get the middle segment
    intersection = three_horizontal.intersection(inv_map_[4])
    seg2letter['M'] = extract(intersection)

    # and now we can get bottom horizontal segment
    top_2 = seg2letter['H'].union(seg2letter['M'])
    seg2letter['B'] = three_horizontal - top_2

    # at this stage we can build the 0
    ss_ = seg2letter['H'].union(seg2letter['B']).union(four_vertical)
    map_[ss_] = 0
    inv_map_[0] = ss_
    six_segs = [frozenset(s) for s in ten_strings if len(s) == 6]

    # the 0 minus the 4 minus 3-horizontal leaves bottom left edge only
    seg2letter['BL'] = inv_map_[0] - three_horizontal - inv_map_[4]

    # the 9 is the set which doesn't contain BL segment
    nine = extract([s for s in six_segs if seg2letter['BL'] not in s])
    map_[nine] = 9
    inv_map_[9] = nine

    # 6 is the last one of the 6-seg digits
    six = extract([s for s in six_segs if s not in {inv_map_[0], nine}])
    map_[six] = 6
    inv_map_[6] = six

    # 2 is the only 5-seg digit with bottom left edge
    two = extract([s for s in five_segments if extract(seg2letter['BL']) in s])
    map_[two] = 2
    inv_map_[2] = two

    # to distinguish between 3 and 5, we intersect with 6.
    with_six = [s.intersection(six) for s in five_segments if s != two]
    three = extract(s for s in with_six if len(s) == 4)
    five = extract(s for s in with_six if len(s) == 5)
    map_[three] = 3
    inv_map_[3] = three
    map_[five] = 5
    inv_map_[5] = five
    return map_


def main_f(fname):
    summ = 0
    with open(fname, 'rt') as fh:
        for line in fh:
            first_part, last_part = line.split(' | ')
            ten_digits = first_part.split()
            four_digits = last_part.split()[:4]
            mapping = learn_mapping(ten_digits)
            pprint(mapping)
            summ += sum(mapping[frozenset(fd)] for fd in four_digits)
    return summ


if __name__ == "__main__":
    import sys
    print(main_f(sys.argv[1]))
