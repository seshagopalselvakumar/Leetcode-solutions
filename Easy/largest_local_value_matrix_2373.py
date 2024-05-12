#Accepted 12.05.24, 138 ms, 17.2 MB
#Could be better, felt like writing two functions makes the for loops better
def largestLocal(grid):
    n = len(grid)
    #Create a pre-defined grid to save some time
    answer = [[0 for i in range(n-2)] for j in range(n-2)]
    def calc_max(row_min, col_min):
        localMax = 0
        for i in range(row_min, row_min+3):
            for j in range(col_min, col_min+3):
                if grid[i][j] >= localMax:
                    localMax = grid[i][j]
        return localMax
    
    def driver_func(mid):
        if mid == 0:
            answer[0][0] = calc_max(0,0)
        for i in range(mid):
            for j in range(mid):
                answer[i][j] = calc_max(i, j)

    mid = 0
    if n == 3:
        driver_func(0)
    else:
        mid = n - 2
    
    print(n, mid)
    driver_func(mid)
            
    return answer


def main():
    print(largestLocal([[20,8,20,6,16,16,7,16,8,10],[12,15,13,10,20,9,6,18,17,6],[12,4,10,13,20,11,15,5,17,1],[7,10,14,14,16,5,1,7,3,11],[16,2,9,15,9,8,6,1,7,15],[18,15,18,8,12,17,19,7,7,8],[19,11,15,16,1,3,7,4,7,11],[11,6,5,14,12,18,3,20,14,6],[4,4,19,6,17,12,8,8,18,8],[19,15,14,11,11,13,12,6,16,19]]))

main()