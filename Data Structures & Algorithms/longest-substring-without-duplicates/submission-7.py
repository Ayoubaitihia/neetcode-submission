class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_lenght = 1

        left = 0

        leng = 0

        seen = set()

        if not s:
            return 0

        for right in range(len(s)):


            if s[right] not in seen:
                seen.add(s[right])
                leng = right - left + 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                leng = right - left + 1

            if leng > max_lenght:
                max_lenght = leng

        return max_lenght