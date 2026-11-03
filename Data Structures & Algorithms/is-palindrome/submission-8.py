class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []

        for c in s:

            if c.isalnum():
                stack.append(c)

        i = 0
        j = len(stack) - 1

        while i < j:

            if stack[i].lower() != stack[j].lower():
                return False

            i += 1
            j -= 1

        return True
