class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of the minimum price 
        profit = 0
        # Min prices right now and check if the price in the iteration is
        min_price = prices[0]
    
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif (prices[i] - min_price) > profit:
                profit = (prices[i] -  min_price)

        return profit

    