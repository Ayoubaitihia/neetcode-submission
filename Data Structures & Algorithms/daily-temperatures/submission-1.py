class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = []

        i = 0
        j = 0
        count = 0

        while i < len(temperatures) - 1:
            j = i + 1
            count = 0
            while j < len(temperatures):
                
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
                else:
                    j += 1
            
            output.append(count)
            i += 1
        output.append(0)
        return output
