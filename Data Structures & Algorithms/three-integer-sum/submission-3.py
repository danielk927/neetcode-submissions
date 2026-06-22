class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range (len(nums) -1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sumVal = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == sumVal:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 
                elif nums[l] + nums[r] < sumVal:
                    l += 1 
                elif nums[l] + nums[r] > sumVal:
                    r -= 1 
        return result