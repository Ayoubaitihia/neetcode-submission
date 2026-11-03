class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        i = 1

        stack.append(s[0])

        while i < len(s):
            if(len(stack) == 0 and s[i] in open):
                stack.append(s[i])
            elif (len(stack) == 0 and s[i] in close):
                return False
            elif (s[i] in open and stack[-1] in open):
                stack.append(s[i])
            elif (s[i] == '}' and stack[-1] == '{'):
                stack.pop()
            elif (s[i] == ']' and stack[-1] == '['):
                stack.pop()
            elif (s[i] == ')' and stack[-1] == '('):
                stack.pop()
            else:
                return False

            i += 1
        return (len(stack) == 0)