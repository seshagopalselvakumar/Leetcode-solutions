def findRelativeRanks(score):
    l = len(score)
    ranks = [None] * l
    order = sorted(score, reverse= True)

    for i in range(l):
        if score[i] == order[0]:
            ranks[i] = "Gold Medal"
        elif score[i] == order[1]:
            ranks[i] = "Silver Medal"
        elif score[i] == order[2]:
            ranks[i] = "Bronze Medal"
        else:
            ranks[i] = str(order.index(score[i]) + 1)

    return ranks

def main():
    print(findRelativeRanks([10,3,8,9,4]))


main()