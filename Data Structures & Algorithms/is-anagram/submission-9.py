class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        d1 = {}

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for char in t:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
        return d1 == d
        
                