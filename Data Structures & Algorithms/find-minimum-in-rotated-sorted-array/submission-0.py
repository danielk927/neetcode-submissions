class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            val = nums[i]
            res = min(res, val)
        return res