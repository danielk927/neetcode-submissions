class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0 
        numSet = set() 

        while r < len(nums): 
            if abs(l - r) > k: 
                numSet.remove(nums[l])
                l += 1 
            if nums[r] in numSet: 
                return True 
            else: 
                numSet.add(nums[r])
                r += 1 
        return False

        