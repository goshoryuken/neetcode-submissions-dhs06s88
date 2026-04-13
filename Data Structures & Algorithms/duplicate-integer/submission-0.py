class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dic = {}

        for num in nums:
            if (num not in my_dic):
                my_dic[num] = 0
            else:
                my_dic[num] += 1
            
            if (my_dic[num] > 0):
                return True

        return False;

        