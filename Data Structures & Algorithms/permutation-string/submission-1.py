class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        freq1 = {}
        windowCount = {}

        windowSize = len(s1)

        for c in s1:
            freq1[c] = freq1.get(c,0) + 1
        
        for i in range(windowSize):
            windowCount[s2[i]] = windowCount.get(s2[i],0) + 1 

        if freq1 == windowCount:
            return True
            
        for r in range(windowSize, len(s2)):
            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1
            l = r - windowSize
            windowCount[s2[l]] -= 1 
            
            if windowCount[s2[l]] == 0: 
                del windowCount[s2[l]]

            if freq1 == windowCount:
                return True
        return False

