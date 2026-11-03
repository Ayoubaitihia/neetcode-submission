class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        i = 0

        stack = []

        result = 0

        for token in tokens:
            if token in '+-*/':
                if token == '+':
                    result = int(stack[-2] + stack[-1])
                elif token == '-':
                    result = int(stack[-2] - stack[-1])
                elif token == '*':
                    result = int(stack[-2] * stack[-1])
                elif token == '/':
                    result = int(stack[-2] / stack[-1])

                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))


        return stack[-1]
