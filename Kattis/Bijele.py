#! /usr/bin/python3

import sys

def main():
    correct = [1, 1, 2, 2, 2, 8]
    pieces = list(map(int, input().split()))
    for i in range(len(pieces)):
        print(correct[i] - pieces[i], end=(" " if i != len(pieces) - 1 else ""))

if __name__ == "__main__":
    main()