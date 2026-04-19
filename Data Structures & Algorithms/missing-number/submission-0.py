class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        da_range = len(nums)

        r = []

        for i in range(da_range + 1):
            r.append(i)

        for num in nums:
            if num in r:
                r.remove(num)

        return r[0]


        