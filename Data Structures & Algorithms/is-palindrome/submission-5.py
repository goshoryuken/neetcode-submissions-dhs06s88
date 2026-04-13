class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        
        theFinal = ""

        for letter in s:
            if letter.isalnum():
                theFinal += letter
                
        theFinal = theFinal.lower()
        left = 0
        right = len(theFinal) - 1
        
        while left <= right:
            if theFinal[left] != theFinal[right]:
                return False
            left += 1
            right -= 1
        return True

