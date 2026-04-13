class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        
        
        max_freq = 0
        freq = {}
        max_len = 0

        

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 - max_freq > k:
                if freq[s[l]] == 1:
                    del freq[s[l]]
                else:
                    freq[s[l]] -= 1
                l += 1
            max_len = max(r - l + 1, max_len)
            
            
        return max_len
            
            


            








        