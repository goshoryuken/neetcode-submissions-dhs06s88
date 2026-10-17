class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []

        for word in strs:
            lst = [0] * 26
            
            for char in word:
                lst[ord(char) - ord('a')] += 1
            
            tup = tuple(lst)

            if tup not in d:
                d[tup] = [word]
            else:
                d[tup].append(word)
        
        for val in d.values():
            result.append(val)
        return result

        