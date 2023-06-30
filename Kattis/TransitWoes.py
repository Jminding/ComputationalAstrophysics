#! /usr/bin/python3

import sys

def main():
    s, t, n = map(int, input().split())
    d = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    time_taken = 0
    for i in range(n):
        time_taken += d[i]
        time_taken += (c[i] - time_taken % c[i]) % c[i]
        time_taken += b[i]

    time_taken += d[-1]
    print("yes" if time_taken <= t - s else "no")

if __name__ == "__main__":
    main()