class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        if len(s1) > len(s2):
            return False

        s1_freq = {}

        for char in s1:
            if char not in s1_freq:
                s1_freq[char] = 0
            else:
                s1_freq[char] += 1

        while r < len(s2):
            j = l
            sub_freq = {}
            while j <= r:
                if s2[j] not in sub_freq:
                    sub_freq[s2[j]] = 0
                else:
                    sub_freq[s2[j]] += 1
                j += 1
            if sub_freq == s1_freq:
                return True
            l += 1
            r += 1

        return False


        
        
            
        