class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        d = []
        streak = 0


        for i in range(len(nums)):
            if nums[i] == 1 and i != len(nums) - 1:
                streak += 1
            else:
                if i == len(nums) - 1 and nums[i] == 1:
                    streak += 1
                    d.append(streak)
                    break
                d.append(streak)
                streak = 0


        return max(d);
        