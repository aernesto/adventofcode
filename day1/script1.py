# -*- coding: utf-8 -*-


def output(fname):
    increase = 0
    with open(fname, 'rt') as fh:
        for i, line in enumerate(fh):
            if i == 0:
                current = int(line)
                continue

            last = current
            current = int(line)
            increase += current > last
    print(f"Total lines = {i + 1}")
    return increase


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print(output(filename))
