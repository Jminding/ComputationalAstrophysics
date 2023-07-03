#! /usr/bin/python3

import sys

def main():
    x, y, x1, y1, x2, y2 = list(map(int, input().split()))
    x_dist, y_dist = 0, 0
    if (x > x1 and x2 > x):
        x_dist = 0
    elif (x <= x1):
        x_dist = x1 - x
    else:
        x_dist = x2 - x
    if (y > y1 and y2 > y):
        y_dist = 0
    elif (y <= y1):
        y_dist = y1 - y
    else:
        y_dist = y2 - y
    print(round((x_dist ** 2 + y_dist ** 2) ** 0.5, 3))
    

if __name__ == "__main__":
    main()