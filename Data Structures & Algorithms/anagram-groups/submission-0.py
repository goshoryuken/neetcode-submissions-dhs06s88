class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            
            d = {}

            for word in strs:
                count = [0] * 26
                for char in word:
                    count[ord(char) - ord('a')] += 1
                key = tuple(count)
                if key not in d:
                    d[key] = [word]
                else:
                    d[key].append(word)
            
            result = []

            for value in d.values():
                result.append(value)

            return result
            
                

                


            
            





        

        