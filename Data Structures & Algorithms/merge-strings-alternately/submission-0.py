class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        res = [] 
        if len(word1) > len(word2):
            longS = word1
            shortS = word2 
        else:
            longS = word2
            shortS = word1
        
        for i in range(len(shortS)): 
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(longS[len(shortS):])
        return "".join(res)
