class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        max_counter = 0

        for num in set_num:
            if num - 1 not in set_num:
                current = num
                counter = 1

                while current + 1 in set_num:
                    current += 1
                    counter += 1
                max_counter = max(counter, max_counter)

        return max_counter