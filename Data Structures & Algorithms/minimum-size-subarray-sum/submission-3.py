class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        currSum = 0 
        left = 0 

        for right in range(len(nums)): 
            currSum += nums[right] 

            while currSum >= target: 
                res = min(res, right - left + 1)
                currSum -= nums[left]
                left += 1 

        if res == float("inf"): 
            return 0 
        return res
