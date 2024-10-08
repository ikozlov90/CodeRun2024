import sys


def main():
    nums = list(map(int, input().split()))
    count = 0
    for i in range(1, len(nums) - 1):
        if (nums[i] > max(nums[i-1], nums[i+1])):
            count += 1
    print(count)
    return

if __name__ == '__main__':
    main()
