import sys


def main():
    synonims = {}
    n = int(input())
    for _ in range(n):
        word1, word2 = input().split()
        synonims[word1] = word2
        synonims[word2] = word1
    print(synonims[input()])


if __name__ == '__main__':
    main()
