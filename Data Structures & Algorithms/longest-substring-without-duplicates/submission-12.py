class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        letters = set() 
        longest = 0

        while r < len(s): 
            if s[r] not in letters:
                letters.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1 
            else:
                letters.discard(s[l])
                l += 1 
        return longest
                


            