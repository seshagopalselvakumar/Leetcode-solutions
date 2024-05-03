#Accepted: 03.05.24, 46ms, 16.52 MB
def addedInteger(nums1, nums2):
    #Solution 1: return the average difference value
    l = len(nums1)
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    return (sum2-sum1) // l

    #Solution 2: sort the lists and return the difference of the values at the first index
    nums1.sort()
    nums2.sort()
    return nums2[0] - nums1[0]

def main():
    print(addedInteger([10], [5]))

main()