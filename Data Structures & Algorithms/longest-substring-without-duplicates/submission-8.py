class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        longest = 0
        wordSet = set()

        while r < len(s): 
            if s[r] not in wordSet: 
                wordSet.add(s[r])
                longest = max(longest, r - l + 1 )
                r += 1 
            else:
                wordSet.discard(s[l])
                l += 1

        return longest
            