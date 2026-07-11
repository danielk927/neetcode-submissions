class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2): 
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i - 1] == nums[i]: 
                continue 
            while l < r: 
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1 
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1 
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1 
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1 
                else:
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
        return res
