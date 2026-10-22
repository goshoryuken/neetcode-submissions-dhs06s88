class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []
        
        for i in range(n):
            res.append(1)
        #find the product of everything to the left

        left = 1
        for i in range(n):
            res[i] = left
            left = left * nums[i]

        right = 1
        i = n - 1

        while i >= 0:
            res[i] = res[i] * right
            right = right * nums[i]
            i -= 1
        return res





        