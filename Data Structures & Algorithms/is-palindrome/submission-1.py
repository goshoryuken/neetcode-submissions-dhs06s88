class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        backward = ""
        nospace_str = s.replace(" ", "")
        new_str = nospace_str.lower()
        alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        for letter in new_str:
            if letter not in alphanumeric:
                new_str = new_str.replace(letter, "")

        print(new_str)

        for i in range(len(new_str)):
            forward += new_str[i]
        for j in range(len(new_str) - 1, -1, -1):
            backward += new_str[j]

        print(forward)
        print(backward)

        return forward == backward
        