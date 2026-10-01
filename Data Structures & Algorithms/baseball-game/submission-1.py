class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for op in operations: 
            if op != '+' and op != 'C' and op != 'D':
                s.append(op) 
            elif op == '+': 
                temp1 = s.pop()
                temp2 = s[-1]
                s.append(temp1)
                s.append(int(temp1) + int(temp2))
            elif op == 'C': 
                s.pop() 
            elif op == 'D':
                temp1 = s[-1]
                s.append(int(temp1) * 2)
        
        if not s: 
            return 0 
        res = 0 
        for num in s: 
            res += int(num)
        return res

            
