class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed = "}])"
        

        if len(s) == 1:
            return False
        

        for l in s:
            if l == "(" or l == "[" or l == "{":
                stack.append(l)
            else:
                if not stack:
                    return False

                open_bracket = stack.pop()
                if l == ")":
                    if open_bracket != "(":
                        return False
                elif l == "]":
                    if open_bracket != "[":
                        return False
                elif l == "}":
                    if open_bracket != "{":
                        return False
        
        return len(stack) == 0
      
                
        