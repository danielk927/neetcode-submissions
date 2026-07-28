class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if not nums:
            return 0

        maxlen = 1

        
        for num in numset: 
            if num - 1 in numset: 
                continue
            else:
                len = 1 
                while num + len in numset: 
                    len += 1 
                    maxlen = max(maxlen, len)
        #maxlen = max(maxlen, len)
        return maxlen
