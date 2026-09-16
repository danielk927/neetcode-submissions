class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs: 
            count = 0 
            while count < len(prefix) and count < len(word) and word[count] == prefix[count]: 
                count += 1 
            prefix = prefix[:count]
        return prefix