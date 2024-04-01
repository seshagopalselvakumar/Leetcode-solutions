def sumOfTheDigitsOfHarshadNumber(x):
    #With string conversion
    x_str = str(x)
    total = 0
    for ch in x_str:
        total += int(ch)
        
    return total if x%total == 0 else -1
    
    
    #Without string conversion
    total = 0
    temp = x
    while temp > 0:
        total += temp % 10
        temp //= 10
    
    return total if x % total == 0 else -1

def main():
    print(sumOfTheDigitsOfHarshadNumber(23))

main()