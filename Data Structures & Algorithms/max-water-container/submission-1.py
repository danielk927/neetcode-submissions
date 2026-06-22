class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        
        while l < r: 
            if heights[l] < heights[r]:
                height = heights[l]
                l += 1
            elif heights[l] >= heights[r]:
                height = heights[r]
                r -= 1
            
            
            area = height * (r-l + 1)

            if maxArea < area:
                maxArea = area
        return maxArea
