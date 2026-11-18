class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i, num in enumerate(nums):

            missing = target - num

            if missing in hashMap.keys():
                return [hashMap[missing], i]
            else:
                hashMap[num] = i