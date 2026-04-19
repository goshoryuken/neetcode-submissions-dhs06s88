class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        r = {}

        for i in range(len(nums) + 1):
            r[i] = 0

            

        for num in nums:
            if num in r:
                r[num] += 1

        for key, value in r.items():
            if value == 0:
                return key
            