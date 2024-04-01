def isSubstringPresent(s):
    s_reverse = s[::-1]
    left = 0
    right = left + 1
    while right < len(s):
        sub_str = s_reverse[left:right+1]
        if sub_str in s:
            return True
        left += 1
        right += 1
    
    return False
    
def main():
    print(isSubstringPresent("abcd"))

main()