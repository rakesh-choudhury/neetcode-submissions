class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]
        l = 0
        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                i = stack.pop()
                output[i] = r-i
            stack.append(r)
        return output
