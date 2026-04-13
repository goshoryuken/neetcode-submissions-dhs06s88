class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        final_list = []

        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                dic[num] += 1

        i = 0

        while i < k:
            max_key = max(dic, key=dic.get)
            final_list.append(max_key)
            del dic[max_key]
            i += 1 

        return final_list    
        

            
            



        