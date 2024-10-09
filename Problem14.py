import sys

def get_top3(nums):
    max1 = max2 = max3 = float('-inf')
    for num in nums:
        if num >= max1:
            max1, max2, max3 = num, max1, max2
        elif num >= max2:
            max1, max2, max3 = max1, num, max2
        elif num >= max3:
            max1, max2, max3 = max1, max2, num
    return max1, max2, max3

def minus(nums):
    return [-num for num in nums]
    
def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

def main():
    nums = list(map(int, input().split()))
    max1, max2, max3 = get_top3(nums) 
    min1, min2, min3 = minus(get_top3(minus(nums)))
    triples = [[max1, max2, max3], [max1, max2, min1], 
        [min1, min2, min3], [min1, min2, max1]]
    prods = [a*b*c for [a,b,c] in triples]
    print(' '.join(map(str, triples[argmax(prods)])))

if __name__ == '__main__':
    main()
