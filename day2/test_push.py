# -*- coding: utf-8 -*-
from collections import deque


def antiguo(fname):
    increase = 0
    for i, line in enumerate(fname):
        if i == 0:
            current = line
            continue

        last = current
        current = line
        increase += current > last
    print(f"Total lines = {i + 1}")
    return increase


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    queue = deque([], 3)

    sums = []
    with open(filename, 'rt') as array:
        for step, element in enumerate(array):
            queue.append(int(element))
            if step < 2:
                continue
            sums.append(sum(queue))

    print(antiguo(sums))
