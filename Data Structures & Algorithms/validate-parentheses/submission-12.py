class Solution:

    def isAlpha(self, c: str) -> bool:
        if 'a' <= c <= 'z':
            return True
        elif 'A' <= c <= 'Z':
            return True
        elif '0' <= c <= '9':
            return True
        else:
            return False


    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for char in s:
            if char in '({[' :
                stack.append(char)
            else :
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return (len(stack) == 0)