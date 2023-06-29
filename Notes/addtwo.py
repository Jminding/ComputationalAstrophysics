#! /usr/bin/python3

import sys

def main():
    # line = sys.stdin.readline()
    # line = line.strip()
    # num = line.split()
    # a = int(num[0])
    # b = int(num[1])
    a, b = map(int, input().strip().split())
    print(a + b)

if __name__ == "__main__":
    main()