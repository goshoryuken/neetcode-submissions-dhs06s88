class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {};
        d1 = {};

        if len(s) != len(t):
            return False

        i = 0;
        while i < len(s):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            
            if t[i] not in d1:
                d1[t[i]] = 1
            else:
                d1[t[i]] += 1
            i += 1
        
        return d == d1
        