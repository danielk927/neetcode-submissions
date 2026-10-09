class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currSum = 0 
        hashMap = defaultdict(int)
        hashMap[0] = 1 

        for i in range(len(nums)): 
            currSum += nums[i]

            if currSum - k in hashMap: 
                res += hashMap[currSum - k]

            hashMap[currSum] += 1 
        
        return res