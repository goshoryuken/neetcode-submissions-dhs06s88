class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"

        s = s.lower()
        s = s.replace(" ", "")

        i = 0
        j = len(s) - 1 

        s1 = ""
        s2 = ""

        while i < len(s):

            if s[i] in alphanum:
                s1 += s[i]

            if s[j] in alphanum:
                s2 += s[j]

            i += 1
            j -= 1
        print(s1)
        print(s2)
        return s1 == s2


        