# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    x, y, aim = 0, 0, 0
    with open(sys.argv[1], 'rt') as fh:
        for line in fh:
            word, number = line.split()
            number = int(number)
            #  print(word, number)
            if word == 'up':
                aim -= number
            if word == 'down':
                aim += number
            if word == 'forward':
                x += number
                y += aim * number
    print(x, y, x * y)
