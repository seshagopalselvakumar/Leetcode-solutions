def lengthOfLastWord(s):
    s_split = s.strip().split(" ")
    return len(s_split[-1])

def main():
    print(lengthOfLastWord("   fly me   to   the moon  "))

main()