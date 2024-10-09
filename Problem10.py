import sys
from math import gcd

def main():
    a, b = map(int, input().split())
    d = gcd(a,b)
    print(d, a * b // d)


if __name__ == '__main__':
    main()
