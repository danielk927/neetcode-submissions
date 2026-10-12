class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        hashMap = defaultdict(list)
        for num in arr: 
            hashMap[abs(x - num)].append(num) 
        #diff : num

        count = 0 
        while len(res) < k: 
            if count in hashMap: 
                for num in hashMap[count]: 
                    res.append(num)
                    if len(res) == k:
                        break
            count += 1 
        return sorted(res)

