#! /usr/bin/python3

import sys

def main():
    l = list(map(int, input().split()))
    print(min(l) * sorted(l)[-2])

if __name__ == "__main__":
    main()