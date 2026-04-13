class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        char_set = set()
        max_len = 0


        for r in range(len(s)):
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1

            char_set.add(s[r])

            current = len(char_set)
            max_len = max(current, max_len)

        return max_len
                
            

