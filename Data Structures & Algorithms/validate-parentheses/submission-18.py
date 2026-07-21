class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}

        for brackets in s: 
            if brackets in closeToOpen: 
                if stack and closeToOpen[brackets] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(brackets)

        if stack:
            return False
        else:
            return True
