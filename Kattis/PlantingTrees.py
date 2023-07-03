#! /usr/bin/python3

import sys

def main():
    n = int(input())
    trees = map(int, input().split())
    trees_sorted = sorted(trees, reverse=True)
    days = [trees_sorted[i] + i + 2 for i in range(n)]
    print(max(days))

if __name__ == "__main__":
    main()