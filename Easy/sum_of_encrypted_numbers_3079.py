def sumOfEncrypterInt(nums):
    def encrypt(x):
        x = str(x)
        template = len(x) * "1"
        max_digit = 0
        for digit in x:
            if int(digit) > max_digit:
                max_digit = int(digit)
        
        return int(template) * max_digit
    
    answer = 0
    for num in nums:
        answer += encrypt(num)
    
    return answer

def main():
    print(sumOfEncrypterInt([1,2,3]))

main()