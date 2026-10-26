class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        running = 0
       
        max_sum = nums[0]

        for num in nums:
            if running < 0:
                running = num
            else:
                running += num
            max_sum = max(running, max_sum)

        return max_sum
        
        
            
        