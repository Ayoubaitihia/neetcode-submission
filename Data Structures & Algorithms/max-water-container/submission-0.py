class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        values = []

        left = 0
        right = len(heights) - 1

        max_value = 0

        while left < right:
            value = (right - left) * (min(heights[left], heights[right]))

            if value > max_value:
                max_value = value
    
            # print("Left:", heights[left])
            # print("right:", heights[right])

            # print("Value:", value)

            values.append(value)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

            # print("==========")

        return max_value