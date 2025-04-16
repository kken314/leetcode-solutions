class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operators:
                if token == '+':
                    temp = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                elif token == '-':
                    temp = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                elif token == '*':
                    temp = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                else:
                    temp = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
            else:
                stack.append(int(token))
            
        return int(stack[0])
        