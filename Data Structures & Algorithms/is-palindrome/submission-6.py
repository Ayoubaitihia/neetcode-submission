class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        
        newStr = []
        i = 0

        for char in s:
            if char.isalnum():
                newStr.append(char.upper())

        if not newStr:
            return True

        while (i < (len(newStr) / 2)):
            if (newStr[i] != newStr[len(newStr) - i - 1]):
                return False
            i += 1
        return True