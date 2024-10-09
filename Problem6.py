import sys


def main():
    x, y, z = map(int, input().split())
    num = input()
    digits = [0] * 10
    for i in [x, y , z]:
        digits[i] = 1
    for d in num:
        digits[int(d)] = 1
    print(max(0, sum(digits) - 3))
    


if __name__ == '__main__':
    main()
