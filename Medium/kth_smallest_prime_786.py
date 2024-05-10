#Accepted, O(N2), 3105 ms, 173.9 MB
#Code not good, need to work on the algorithm - maybe read the editorial!
def kthSmallestPrimeFraction(arr, k):
    hmap = dict()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            
            hmap[arr[i]/arr[j]] = [arr[i], arr[j]]

    val = dict(sorted(hmap.items()))
    for i in range(len(val.values())):
        if i == (k-1):
            return list(val.values())[i]



def main():
    print(kthSmallestPrimeFraction([1,2,3,5], 3))

main()