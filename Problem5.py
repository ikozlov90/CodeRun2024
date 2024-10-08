import sys
from math import sqrt

def main():
    a, b, c = map(int, input().split())
    d = b**2 - 4*a*c
    if (d < 0):
        print(0)
        return
    elif (d == 0):
        print(1)
        print(format(-b / (2.0 * a), '.6f'))
    else:
        lroot = (-b - sqrt(d)) / (2.0 * a)
        rroot = (-b + sqrt(d)) / (2.0 * a)
        print(2)
        print(format(lroot, '.6f'), format(rroot, '.6f')) 

if __name__ == '__main__':
    main()
