def isIsomorphic(s,t):
    def calc_validity(str1, str2):
        l = len(s)
        hmap = dict()
        for i in range(l):
            if str1[i] not in hmap:
                hmap[str1[i]] = str2[i]
            else:
                if hmap[str1[i]] != str2[i]:
                    return False
        return True

    val1 = calc_validity(s,t)
    val2 = calc_validity(t,s)

    return val1 and val2
    
def main():
    print(isIsomorphic("aaabbbab", "bbbaaaab"))


main()