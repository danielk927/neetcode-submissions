class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {} 
        for i in range(len(s)): 
            if s[i] in hashMap: 
                hashMap[s[i]] += 1 
            else:
                hashMap[s[i]] = 1
        for i in range(len(s)): 
            if hashMap[s[i]] == 1: 
                return i
        return -1