class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for num in nums: 
            if num == 0: 
                r += 1 
            if num == 1: 
                w += 1 
            if num == 2: 
                b += 1 
        nums[:r] = [0] * r
        nums[r:w + r] = [1] * w
        nums[w + r:] = [2] * b