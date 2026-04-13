class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.lower();
        new_str = new_str.replace(" ", "")



        first = ""
        for char in new_str:
            ordi = ord(char)
            if ordi >= 48 and ordi < 58 or ordi >= 97 and ordi < 123:
                first += char

        second = ""
        for i in range(len(new_str) - 1, -1, -1):
            ordi = ord(new_str[i])
            if ordi >= 48 and ordi < 58 or ordi >= 97 and ordi < 123:
                second += new_str[i]


        print(first)
        print(second)
        return first == second

        