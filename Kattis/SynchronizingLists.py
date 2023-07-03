#! /usr/bin/python3

import sys

def main():
    while True:
        n = int(input())
        list1 = []
        list2 = []
        if n == 0:
            break
        for _ in range(n):
            list1.append(int(input()))
        for _ in range(n):
            list2.append(int(input()))
        list1_sorted = sorted(list1)
        list2_sorted = sorted(list2)
        correspondences = {x: y for x, y in zip(list1_sorted, list2_sorted)}
        for i in range(n):
            print(correspondences[list1[i]])
        

if __name__ == "__main__":
    main()