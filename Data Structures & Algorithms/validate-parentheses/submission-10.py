class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in close_to_open: #check keys in dict if closing bracket
                # if stack aint empty AND if top of stack has the value of the dict
                #(the opening bracket)
                if stack and stack[-1] == close_to_open[char]: 
                    stack.pop() #remove matched bracket
                else:
                    return False #if it dont match
            else: #if instead its an opening bracket, add to stack
                stack.append(char)

        return not stack #if stack is empty, its valid


                    
