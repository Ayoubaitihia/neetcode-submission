class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup_nums = set(nums)

        return len(dup_nums) != len(nums)


nums = [1, 2, 3, 3]

sol = Solution()

sol.hasDuplicate(nums)