#Accepted, 5975 ms, 42.84 MB
#Basic greedy algorithm, but can be further optimized!  
def maximumHappinessSum(happiness, k):
    count = 0
    happiness_sum = 0
    happiness.sort(reverse = True)
    while count < k and len(happiness) > 0:
        if count > 0:
            if (happiness[0] - count) >= 0:
                happiness_sum += happiness[0] - count
            else:
                happiness_sum += 0
        else:
            happiness_sum += happiness[0]
        happiness.pop(0)
        print(count, happiness_sum, happiness)
        count += 1
    
    return happiness_sum

def main():
    print(maximumHappinessSum([12,1,42], 3))

main()