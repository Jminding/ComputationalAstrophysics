#! /usr/bin/python3

import sys

def main():
    dominant = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
    nondominant = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
    n, b = input().split()
    cards = []
    for i in range(4 * int(n)):
        cards.append(input())
    
    points = 0
    for card in cards:
        points += dominant[card[0]] if card[1] == b else nondominant[card[0]]
    print(points)

if __name__ == "__main__":
    main()