class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        prefix = [nums[0]] * len(nums)
        hashMap = defaultdict(int) 
        
        #creating prefix array + hashMap
        for i in range(1, len(nums)): 
            prefix[i] = prefix[i - 1] + nums[i]
        
        hashMap[0] = 1

        for i in range(len(prefix)): 
            if (prefix[i] - k) in hashMap: 
                res += hashMap[prefix[i] - k]
            hashMap[prefix[i]] += 1 
        return res