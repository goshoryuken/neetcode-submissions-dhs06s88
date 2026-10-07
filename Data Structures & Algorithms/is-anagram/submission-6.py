class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        d1 = {}
        d2 = {}

        for letter in s:
            if letter not in d1:
                d1[letter] = 1
            else:
                d1[letter] += 1
        
        for letter in t:
            if letter not in d2:
                d2[letter] = 1
            else:
                d2[letter] += 1
                
        return d1 == d2


        