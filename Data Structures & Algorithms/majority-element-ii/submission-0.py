class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thresh = len(nums) // 3
        res = []
        freqMap = {} 
        for num in nums: 
            freqMap[num] = freqMap.get(num, 0) + 1 
        
        for key in freqMap.keys():
            if freqMap[key] > thresh: 
                res.append(key)
        return res

