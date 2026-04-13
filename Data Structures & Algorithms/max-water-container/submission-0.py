class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        daMax = float('-inf')

        while left < right:
            
            if heights[left] > heights[right]:
                daArea = heights[right] * (right - left)
                right -= 1
            else:
                daArea = heights[left] * (right - left)
                left += 1

            if daArea > daMax:
                daMax = daArea

            
        
        return daMax
            


        
        