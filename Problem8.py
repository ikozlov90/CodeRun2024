import sys


def main():
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            print('NO')
            return
    print('YES')
    return


if __name__ == '__main__':
    main()
