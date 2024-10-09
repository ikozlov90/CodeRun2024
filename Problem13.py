import sys

def palindrom(nums):
    for i in range(len(nums)):
        if nums[i] != nums[-i-1]:
            return False
    return True

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if palindrom(nums[i:]):
            print(i)
            print(' '.join(map(str, reversed(nums[:i]))))
            return

if __name__ == '__main__':
    main()
