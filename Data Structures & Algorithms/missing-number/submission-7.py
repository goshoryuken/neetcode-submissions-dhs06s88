class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0

        for num in nums:
            xor ^= num

        for i in range(0, len(nums) + 1):
            xor ^= i

        return xor
        