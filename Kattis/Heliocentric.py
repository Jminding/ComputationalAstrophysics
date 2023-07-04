#! /usr/bin/python3

import sys

def main():
    case = 1
    for line in sys.stdin:
        try:
            e, m = map(int, line.split())
            year = 0
            while e != 0 or m != 0:
                e = (e + 1) % 365
                m = (m + 1) % 687
                year += 1
            print(f"Case {case}: {year}")
            case += 1
        except ValueError:
            break

if __name__ == "__main__":
    main()