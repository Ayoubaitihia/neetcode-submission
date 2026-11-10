class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for num in nums:

            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        result = []

        sor_hashmap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))

        result = list(sor_hashmap.keys())

        return result[:k]