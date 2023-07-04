#! /usr/bin/python3

import sys

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        intervals.append(tuple(map(int, input().split())))
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = -1
    for interval in intervals:
        if interval[0] >= end:
            count += 1
            end = interval[1]
    print(count)

if __name__ == "__main__":
    main()