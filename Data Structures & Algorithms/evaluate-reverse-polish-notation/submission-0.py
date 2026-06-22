class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for value in tokens:
            if value == "+":
                temp1 = stack[-1]
                stack.pop()
                temp2 = stack[-1]
                stack.pop()
                stack.append(temp2 + temp1)
            elif value == "-":
                temp1 = stack[-1]
                stack.pop()
                temp2 = stack[-1]
                stack.pop()
                stack.append(temp2 - temp1)
            elif value == "*":
                temp1 = stack[-1]
                stack.pop()
                temp2 = stack[-1]
                stack.pop()
                stack.append(temp2 * temp1)
            elif value == "/":
                temp1 = stack[-1]
                stack.pop()
                temp2 = stack[-1]
                stack.pop()
                stack.append(int(temp2 / temp1))
            else:
                stack.append(int(value))
        return stack[0]


        