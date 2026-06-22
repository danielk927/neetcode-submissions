class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        charSet = set()
        maxLength = 0

        while r < len(s):
            if s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            else:
                charSet.add(s[r])
                r += 1
                maxLength = max(maxLength, len(charSet))
        return maxLength