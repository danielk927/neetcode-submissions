from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqMap = defaultdict(int)
        freqMap2 = defaultdict(int)

        for i in range(len(s1)):
            freqMap[s1[i]] += 1
            freqMap2[s2[i]] += 1

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            if freqMap == freqMap2:
                return True

            r += 1
            freqMap2[s2[r]] += 1

            freqMap2[s2[l]] -= 1
            if freqMap2[s2[l]] == 0:
                del freqMap2[s2[l]]

            l += 1

        return freqMap == freqMap2