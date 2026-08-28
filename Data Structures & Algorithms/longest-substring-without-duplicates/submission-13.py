class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        longest = 0 
        words = set() 

        while r < len(s): 
            if s[r] not in words: 
                longest = max(longest, r - l + 1)
                words.add(s[r])
                r += 1 
            else: 
                words.discard(s[l])
                l += 1 
        return longest
