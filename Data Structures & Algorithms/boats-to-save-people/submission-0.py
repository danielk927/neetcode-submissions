class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0 
        r = len(people) - 1 
        people = sorted(people)
        res = 0 

        #1, 2, 2, 3, 3  limit = 3
        #X, 2, X, 3, 3

        while l <= r: 
            if people[l] + people[r] <= limit: 
                l += 1 
            r -= 1 
            res += 1 
        return res
            

            