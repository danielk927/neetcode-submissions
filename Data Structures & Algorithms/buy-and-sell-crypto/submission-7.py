class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = l + 1 
        maxProfit = 0 

        while r < len(prices): 
            profit = prices[r] - prices[l]
            
            if prices[l] > prices[r]:
                r += 1 
                l = r -1 
            else: 
                if profit >= maxProfit:
                    maxProfit = profit
                r += 1 
            
        return maxProfit