#! /usr/bin/python3

import sys

def main():
    case = 1
    while True:
        n = int(input())
        if n == 0:
            break
        names = []
        for i in range(n):
            names.append(input())
        names2 = []
        for i in range(1, n, 2):
            names2.append(names[i])
        names = [name for name in names if name not in names2]
        print("SET", str(case))
        for name in names:
            print(name)
        for name in names2[::-1]:
            print(name)
        case += 1



if __name__ == "__main__":
    main()
