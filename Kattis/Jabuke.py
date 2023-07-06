#! /usr/bin/python3

# file: jabuke.py

# name: Jaymin Ding

# ut eid: jd54998

# date 05 Jul 2023

import sys

def main():
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())
    n = int(input())
    trees = []
    for i in range(n):
        trees.append(tuple(map(int, input().split())))
    print(abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2)

    count = 0
    for tree in trees:
        area = abs(xa * (yb - tree[1]) + xb * (tree[1] - ya) + tree[0] * (ya - yb)) / 2 + abs(xa * (tree[1] - yc) + tree[0] * (yc - ya) + xc * (ya - tree[1])) / 2 + abs(tree[0] * (yb - yc) + xb * (yc - tree[1]) + xc * (tree[1] - yb)) / 2
        if area == abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2:
            count += 1
    print(count)

if __name__ == "__main__":

    main()