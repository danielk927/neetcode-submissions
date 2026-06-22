class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        r = l + 1
        res = []

        while r < len(temperatures):
            if temperatures[r] > temperatures[l]:
                res.append(r - l)
                l += 1
                r = l + 1
            elif r == len(temperatures) - 1:
                res.append(0)
                l += 1
                r = l + 1
            else:
                r += 1

        while l < len(temperatures):
            res.append(0)
            l += 1

        return res