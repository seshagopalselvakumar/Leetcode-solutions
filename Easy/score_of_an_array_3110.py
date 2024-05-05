#Accepted 05.05, 40 ms, 16.5 MB
ef scoreOfString(s):
    score = 0
    n = len(s)
    for i in range(1, n):
        score += abs(ord(s[i-1]) - ord(s[i]))

    return score

def main():
    print(scoreOfString("hello"))

main()