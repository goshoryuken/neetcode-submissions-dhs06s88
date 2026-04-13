class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = s.replace(" ", "")
        final = new_str.lower()
        alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        theFinal = ""

        for letter in final:
            if letter in alphanumeric:
                theFinal += letter

        left = 0
        right = len(theFinal) - 1
        

            

        while left <= right:
            if theFinal[left] != theFinal[right]:
                return False
            left += 1
            right -= 1
        return True

