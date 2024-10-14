import sys

def round_up(p, q):
    return p // q if p % q == 0 else p // q + 1

def main():
    vals = [int(input()) for _ in range(3)]
    total = sum([(i + 2) * vals[i] for i in range(len(vals))])
    print(max(0, round_up(7 * sum(vals) - 2 * total, 3)))


if __name__ == '__main__':
    main()
