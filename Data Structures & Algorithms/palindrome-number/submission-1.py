class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        j = len(string) - 1
        for i in range(len(string)):
            if (string[i] != string[j]):
                
                return False
            j -= 1
        return True
        