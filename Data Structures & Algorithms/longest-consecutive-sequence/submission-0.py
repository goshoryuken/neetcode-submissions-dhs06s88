class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                counter = 1

                while current + 1 in num_set:
                    counter += 1
                    current += 1

                longest = max(counter, longest)

        return longest
            
        

        

        