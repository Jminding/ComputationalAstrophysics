#! /usr/bin/python3

import sys

def main():
    n = int(input())
    for _ in range(n):
        line = input().split()
        k = int(line[0])
        line = line[1:]
        print(sum([int(x) for x in line]) - (k - 1))
    
if __name__ == "__main__":
    main()