class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for bracket in s: 
            if bracket in closeToOpen: 
                if stack and closeToOpen[bracket] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        else:
            return True