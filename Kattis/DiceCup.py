#! /usr/bin/python3

import sys

def main():
    n, m = map(int, input().split())
    outcomes = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            outcomes.append(i + j)
    counts = {}
    for i in outcomes:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    max_count = max(counts.values())
    for i in sorted(counts.keys()):
        if counts[i] == max_count:
            print(i)

if __name__ == "__main__":
    main()