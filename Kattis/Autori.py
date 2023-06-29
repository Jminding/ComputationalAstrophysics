#! /usr/bin/python3

import sys

def main():
    print(''.join([x[0] for x in sys.stdin.readline().split('-')]))

if __name__ == "__main__":
    main()