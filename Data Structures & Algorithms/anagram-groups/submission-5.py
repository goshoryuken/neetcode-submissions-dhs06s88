class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        res = []


        for word in strs:
            l = [0] * 26
            for char in word:
                l[ord(char) - ord('a')] += 1
            l_tup = tuple(l)

            if l_tup not in d:
                d[l_tup] = [word]
            else:
                d[l_tup].append(word)
        
        for value in d.values():
            res.append(value)
            
        return res

                
        