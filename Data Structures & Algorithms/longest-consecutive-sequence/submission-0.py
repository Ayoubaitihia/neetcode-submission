class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        numSet = set(nums)
        beginning = []
        longest = 0

        for num in numSet:
            count = 1
            if num - 1 not in numSet:
                i = 1
                while num + i in numSet:
                    count += 1
                    i += 1

            if longest < count:
                longest = count

        return longest