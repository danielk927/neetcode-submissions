class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i, len(prices)):
                sell = prices[j]
                if sell > buy: 
                    profit = sell - buy
                    if maxProfit < profit:
                        maxProfit = profit
        return maxProfit   
                
                    