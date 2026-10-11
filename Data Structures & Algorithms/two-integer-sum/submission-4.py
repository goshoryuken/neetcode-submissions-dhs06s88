class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            other = target - nums[i]

            if other in d:
                return [d[other], i]
            else:
                d[nums[i]] = i

        return 0
        