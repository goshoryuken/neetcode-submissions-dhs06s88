class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        daSum = 0
        nums.sort()
        
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) -  1  
            while left < right:
                sublist = []
                daSum = nums[left] + nums[right] + nums[i]
                
                if daSum == 0:
                    sublist = [nums[left], nums[right], nums[i]]
                    result.append(sublist)
                    left += 1
                    right -= 1
                elif daSum < 0:
                    left += 1
                else:
                    right -= 1
                    
        filtered = []                     
        for lst in result:
            if lst not in filtered:
                filtered.append(lst)
        return filtered
                    

        