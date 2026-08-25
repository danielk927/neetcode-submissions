class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 0 
        maxProfit = 0 

        while r < len(prices): 
            if prices[l] <= prices[r]: 
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1 
            else: 
                r += 1 
                l = r - 1 
        return maxProfit