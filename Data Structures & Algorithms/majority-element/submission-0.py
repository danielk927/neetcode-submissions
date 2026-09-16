class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freqList = defaultdict(int)
        for num in nums: 
            freqList[num] += 1 
            if freqList[num] > n: 
                return num
