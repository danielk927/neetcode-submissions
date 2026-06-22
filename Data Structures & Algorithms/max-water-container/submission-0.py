class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r: 
            if heights[l] < heights[r]:
                height = heights[l]
            if heights[l] >= heights[r]:
                height = heights[r]

            area = height * (r - l)

            if maxArea < area:
                maxArea = area

            if heights[l] < heights[r]: 
                l += 1
            else:
                r -= 1
                
        return maxArea
            
