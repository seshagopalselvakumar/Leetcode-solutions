#Accepted 07.05.24, 3390 ms, 16.9 MB, O(N2)
#Lot of scope for improvement! 
def minOperations(boxes):
    l = len(boxes)
    answer = [0] * l
    for i in range(l):
        for j in range(l):
            if i != j:
                if boxes[j] == "1":
                    answer[i] += abs(i-j)

    return answer

def main():
    print(minOperations("110"))

main()