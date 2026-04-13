class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            difference = target - nums[i];
            if (difference not in d):
                d[nums[i]] = i
            else:
                if (d[difference] < i):
                    return [d[difference], i]
                else:
                    return [i, d[difference]]
            





        