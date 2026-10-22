class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count how often each number appears
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # step 2: make empty buckets, one for each possible frequency
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        # put each number in the bucket matching its frequency
        for num in count:
            freq = count[num]
            buckets[freq].append(num)

        # step 3: go from the highest frequency down, collect k numbers
        result = []
        i = len(buckets) - 1
        while i > 0:
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1

        return result