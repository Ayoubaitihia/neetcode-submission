class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []
        result = []
        product = 1

        for num in nums:
            product *= num
            prefix.append(product)

        product = 1

        for num in nums[::-1]:
            product *= num
            postfix.append(product)

        postfix = postfix[::-1]


        for i, num in enumerate(nums):
            if i == 0:
                a = 1
            else:
                a = prefix[i - 1]
            if i == len(nums) - 1:
                b = 1
            else:
                b = postfix[i + 1]
            res = a * b

            result.append(res)



        return result