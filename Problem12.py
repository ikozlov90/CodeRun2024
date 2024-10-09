import sys

def argmin(iterable):
    return min(enumerate(iterable), key=lambda x: x[1])[0]
    
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    val = int(input())
    dist = [abs(num - val) for num in nums]
    print(nums[argmin(dist)])


if __name__ == '__main__':
    main()
