#accepted, 50ms, 16.5 MB
def minOperations(nums, k):
    nums.sort()
    c = 0
    for num in nums:
        if num < k:
            c += 1
        else:
            return c


def main():
    print(minOperations([2,11,10,1,3], 10))

main()