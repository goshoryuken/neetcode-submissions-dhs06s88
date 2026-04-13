class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        s1_freq = {}
        sub_freq = {}

        if len(s1) > len(s2):
            return False

        for char in s1:
            if char not in s1_freq:
                s1_freq[char] = 1
            else:
                s1_freq[char] += 1

        for i in range(len(s1)):
            if s2[i] not in sub_freq:
                sub_freq[s2[i]] = 1
            else:
                sub_freq[s2[i]] += 1
        
        if sub_freq == s1_freq:
            return True

        while r < len(s2) - 1:
            r += 1
            l += 1

            if s2[r] not in sub_freq:
                sub_freq[s2[r]] = 1
            else:
                sub_freq[s2[r]] += 1

            if sub_freq[s2[l - 1]] == 1:
                del sub_freq[s2[l - 1]]
            else:
                sub_freq[s2[l - 1]] -= 1

            if sub_freq == s1_freq:
                return True
        return False