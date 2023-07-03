#! /usr/bin/python3

import sys

def main():
    alphabet = {
        'a': "2",
        'b': "22",
        'c': "222",
        'd': "3",
        'e': "33",
        'f': "333",
        'g': "4",
        'h': "44",
        'i': "444",
        'j': "5",
        'k': "55",
        'l': "555",
        'm': "6",
        'n': "66",
        'o': "666",
        'p': "7",
        'q': "77",
        'r': "777",
        's': "7777",
        't': "8",
        'u': "88",
        'v': "888",
        'w': "9",
        'x': "99",
        'y': "999",
        'z': "9999",
        ' ': "0"
    }
    n = int(input())
    for i in range(n):
        text = input()
        output = ""
        for j in range(len(text)):
            if j != len(text) - 1 and alphabet[text[j]][0] == alphabet[text[j + 1]][0]:
                output += alphabet[text[j]] + " "
            else:
                output += alphabet[text[j]]
        print("Case #{}: {}".format(i + 1, output))

if __name__ == "__main__":
    main()