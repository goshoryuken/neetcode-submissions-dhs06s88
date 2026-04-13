class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        char_set = set()

        
        biggest = 0

        

        if s == "":
            return 0

        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])
                    
                    
            
            biggest = max(len(char_set), biggest)

            

        return biggest

            

        