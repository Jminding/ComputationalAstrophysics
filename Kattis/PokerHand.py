#! /usr/bin/python3

import sys

def main():
    cards = list(map(lambda x: list(x)[0], input().split()))
    values = {}
    for card in cards:
        if card in values:
            values[card] += 1
        else:
            values[card] = 1
    print(max(values.values()))

if __name__ == "__main__":
    main()