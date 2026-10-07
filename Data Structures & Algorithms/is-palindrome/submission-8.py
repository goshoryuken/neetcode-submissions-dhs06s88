class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        str1 = ""
        str2 = ""

        s = s.lower()
        s.replace(" ", "")
        alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"

        while (i < len(s)):
            if (s[i] in alphanum):
                str1 += s[i]
            if (s[j] in alphanum):
                str2 += s[j]
            
            i += 1
            j -= 1

        return str1 == str2

        