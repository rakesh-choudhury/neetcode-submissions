class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        start_idx = 0
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            start_idx = index
            while stack and height < stack[-1][1]:
                start_idx, h = stack.pop()
                max_area = max(max_area, h * (index-start_idx))
            stack.append((start_idx,height))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        return max_area
