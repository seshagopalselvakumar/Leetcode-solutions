def maxBottlesDrunk(numBottles, numExchange):
    bottles_drunk = numBottles
    empty_bottles = numBottles
    new_bottles = 0
    while (empty_bottles + new_bottles) >= numExchange:
        #print(empty_bottles, new_bottles, numExchange)
        empty_bottles -= numExchange
        new_bottles += 1
        numExchange += 1
    

    return bottles_drunk + new_bottles

def main():
    print(maxBottlesDrunk(13,6))


main()