#Accepted, 58 ms, 16.69 MB, O(n2)
def finalPrices(prices):
    final_prices = prices
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j] <= prices[i]:
                final_prices[i] = prices[i] - prices[j]
                break

    return final_prices

def main():
    print(finalPrices([8,4,6,2,3]))

main()