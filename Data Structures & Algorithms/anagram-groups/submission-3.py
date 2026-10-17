class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #go thru strs, get the char count of each word and put it into its own unique dict
        #then if temp_d is in like a big d then you like add it into a sublsit
        big_d = {}
        end = []


        for word in strs:
            temp = [0] * 26

            for char in word:
                temp[ord(char) - ord('a')] += 1

            key = tuple(temp)
            if key in big_d:
                big_d[key].append(word)
            else:
                big_d[key] = [word]
        
        for key, value in big_d.items():
            end.append(value)
        return end




        