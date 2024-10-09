import sys


def main():
    reader = open('input.txt', 'r')
    words = set()
    for line in reader:
        for word in line.split():
            words.add(word)
    print(len(words))
    reader.close

if __name__ == '__main__':
    main()
