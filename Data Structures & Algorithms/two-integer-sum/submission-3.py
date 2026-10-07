class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #nums[j] = target - nums[i]
        #3, is 4 in d yet? no? add 3
        #4, is 3 in d yet? yes? return d[target], d[i]

        d = {}

        for i in range(len(nums)):
            second = target - nums[i]

            if second in d:
                return [d[second], i]
            else:
                d[nums[i]] = i

        return 0

        