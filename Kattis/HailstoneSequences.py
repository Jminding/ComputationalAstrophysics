#! /usr/bin/python3

import sys

def main():
    n = int(input())
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    print(length)

if __name__ == "__main__":
    main()