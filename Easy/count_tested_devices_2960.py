#Accepted, 109 ms, 16.5 MB, O(n2) complexity
def countTestedDevices(batteryPercentages):
    #Solution 1
    ind = 0
    n = len(batteryPercentages)
    tested_devices = 0
    while ind < n:
        if batteryPercentages[ind] > 0:
            tested_devices += 1
            for j in range(ind+1,n):
                batteryPercentages[j] = max(0, batteryPercentages[j]-1)
        
        ind += 1
    return tested_devices

def main():
    print(countTestedDevices([1,1,2,1,3]))

main()