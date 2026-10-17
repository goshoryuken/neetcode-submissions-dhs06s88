class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #dictionary with like the occurances of each number
        #then loop k times

        result = []
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        i = k
        
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1],))

        while i > 0:
            result.append(next(reversed(sorted_d)))
            sorted_d.popitem()
            i -= 1
        return result

        

        