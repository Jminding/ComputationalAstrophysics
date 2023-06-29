#! /usr/bin/python3

import sys

def main():
    A, I = map(int, input().split())
    print(A * (I - 1) + 1)

if __name__ == "__main__":
    main()