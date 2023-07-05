#! /usr/bin/python3

import sys

def main():
    n = input()
    print(product(n))

def product(n):
    if len(n) == 1:
        return int(n)
    else:
        n = n.replace("0", "")
        x = 1
        for i in n:
            x *= int(i)
        return product(str(x))

if __name__ == "__main__":
    main()