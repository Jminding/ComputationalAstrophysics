#! /usr/bin/python3

# file: pyramids.py

# name: Jaymin Ding

# ut eid: jd54998

# date 26 Jun 2023

import sys

def main():
    blocks = int(input())
    height = 0
    while 4 * (height ** 3) / 3 - height / 3 <= blocks:
        height += 1
    height -= 1
    print(height)


if __name__ == "__main__":
    main()