import sys


def main():
    sides = []
    for i in range(3):
        sides.append(int(input()))
    a, b, c = sorted(sides)
    print('YES') if a + b > c else print('NO')


if __name__ == '__main__':
    main()
