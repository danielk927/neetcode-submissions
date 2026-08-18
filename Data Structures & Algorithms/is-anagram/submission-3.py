class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        for i in range(len(s)): 
            mapS[s[i]] += 1 
        
        for j in range(len(t)): 
            mapT[t[j]] += 1 
        
        if mapS != mapT: 
            return False
        return True