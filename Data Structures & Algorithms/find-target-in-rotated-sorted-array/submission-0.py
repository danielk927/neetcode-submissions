class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 

        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] < nums[r]: # right section is properly sorted
                if nums[m] <= target <= nums[r]: # target is in the sorted part
                    l = m + 1
                else:
                    r = m - 1
            else: # left section is properly sorted
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1