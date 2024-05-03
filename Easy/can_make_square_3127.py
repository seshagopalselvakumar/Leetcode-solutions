#Accepted, 43ms, 16.41 MB
def canMakeSquare(grid):
    def calc_sum(row,col):
        hmap = {"B": 0, "W": 0}
        square = [grid[row_index][col_index], grid[row_index][col_index+1], 
                  grid[row_index+1][col_index], grid[row_index+1][col_index+1]]
        
        for point in square:
            hmap[point] += 1
        
        return 3 in hmap.values() or 4 in hmap.values()
    
    for row_index in range(2):
        for col_index in range(2):
            if calc_sum(row_index, col_index):
                return True
    
    return False

            

def main():
    print(canMakeSquare([["B","B","B"],["B","B","B"],["B","B","B"]]))

main()