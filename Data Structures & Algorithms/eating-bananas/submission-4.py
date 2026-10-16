class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')

        while l <= r: 
            m = (r + l) // 2
            
            time = 0 
            for num in piles: 
                if num % m == 0 and num >= m: 
                    time += num // m
                elif num < m: 
                    time += 1 
                else: 
                    time += (num // m) +  1
            
            if time > h: 
                l = m + 1 
            else: 
                r = m - 1
                res = min(res, m)
        return res

                