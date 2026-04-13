class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        daMax = float('-inf')

        while l < r:
            if heights[l] > heights[r]:
                area = heights[r] * (r - l)
                r -= 1
            else:
                area = heights[l] * (r - l)
                l += 1
            
            daMax = max(area, daMax)
        return daMax
        
        