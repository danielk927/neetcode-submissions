class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)

        for num in nums:
            map[num] += 1 

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in map.items(): 
            buckets[freq].append(num)

        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]: 
                res.append(num)
                if len(res) == k:
                    return res