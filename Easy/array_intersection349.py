def intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))
def main():
    print(intersection([1,2,2,1], [2,2]))

main()