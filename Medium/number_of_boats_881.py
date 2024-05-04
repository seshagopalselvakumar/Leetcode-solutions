def numRescueBoats(people, limit):
    #Solution 1:
    boats = 0
    temp = sorted(people) # can also sort in place with people.sort()
    start = 0
    end = len(temp) - 1
    while start < end:            
        if temp[end] == limit:
            boats += 1
            end -= 1
        else:
            total = temp[start] + temp[end]
            if total == limit:
                boats += 1
                start += 1
                end -=1
            elif total > limit:
                boats += 1
                end -= 1
            else:
                boats += 1
                start += 1
                end -= 1
            
        if (start == end) and temp[end] <= limit:
            boats += 1
            return boats
         
        
    return boats

    #Solution 2:
    while start <= end:   
        boats +=1
        if temp[start] + temp[end] <= limit:
            start += 1
        end -= 1
         
    return boats


def main():
    print(numRescueBoats([2,2], 6))

main()