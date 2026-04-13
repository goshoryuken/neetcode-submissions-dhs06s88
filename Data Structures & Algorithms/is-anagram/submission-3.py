class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        d_1 = {}
        for letter in s:
            if letter not in d:
                d[letter] = 0
            else:
                d[letter] += 1
            
        
        for letter in t:
            if letter not in d_1:
                d_1[letter] = 0
            else:
                d_1[letter] += 1            

        

        return d == d_1
                
