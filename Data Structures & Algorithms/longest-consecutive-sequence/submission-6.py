class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)

        streak = 1
        maxn = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                streak += 1 
            elif nums[i] == nums[i - 1]:
                continue
            else:
                maxn = max(streak, maxn)
                streak = 1
        maxn = max(streak, maxn)
        return maxn

            