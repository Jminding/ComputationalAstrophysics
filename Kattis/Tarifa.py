#! /usr/bin/python3

import sys

def main():
    x = int(input())
    n = int(input())
    sum_p = sum([int(input()) for i in range(n)])
    print((x * (n + 1)) - sum_p)

if __name__ == "__main__":
    main()