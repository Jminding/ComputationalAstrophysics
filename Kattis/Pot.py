#! /usr/bin/python3

import sys

def main():
    n = int(input())
    s = 0
    for i in range(n):
        x = input()
        s += int(x[:len(x) - 1]) ** int(x[-1]) if len(x) > 1 else int(x)
    print(s)

if __name__ == "__main__":
    main()