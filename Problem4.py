import sys


def main():
    n = int(input())
    nums = [1] * n
    for i in range(2, len(nums)):
        nums[i] = nums[i-1] + nums[i-2]
    print(sum(nums))
    return


if __name__ == '__main__':
    main()
