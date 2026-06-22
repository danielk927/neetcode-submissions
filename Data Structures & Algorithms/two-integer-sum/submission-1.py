class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {} 

        for i, n in enumerate(nums):
            complement = target - n

            if complement in numSet:
                return [numSet[complement], i]
            numSet[n] = i 