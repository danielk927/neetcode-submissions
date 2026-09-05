class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        wordSet = set()
        maxLength = 0 

        while r < len(s): 
            if s[r] not in wordSet: 
                maxLength = max(maxLength, r - l + 1)
                wordSet.add(s[r])
                r += 1 
            else: 
                wordSet.discard(s[l])
                l += 1 
        return maxLength