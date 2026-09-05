class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        maxLength = 0
        freqMap = defaultdict(int) 

        for r in range(len(s)):
            freqMap[s[r]] += 1 
            maxFreq = max(freqMap.values())
            while ((r - l + 1 - maxFreq) > k):
                freqMap[s[l]] -= 1
                l += 1 
            maxLength = max(r - l + 1, maxLength)
                
        return maxLength

           
            