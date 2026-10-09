class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list) 

        for word in strs: 
            sortedWord = "".join(sorted(word))
            if sortedWord in wordMap: 
                wordMap[sortedWord].append(word) 
            else:
                wordMap[sortedWord] = [word]
            
        res = [] 
        for val in wordMap.values(): 
            res.append(val) 
        return res


            