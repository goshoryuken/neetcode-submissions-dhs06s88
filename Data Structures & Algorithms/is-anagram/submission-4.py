class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        d1 = {}

        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        
        for letter in t:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1
        return d == d1

        