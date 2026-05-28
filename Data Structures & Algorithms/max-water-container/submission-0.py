class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxarea = 0
        area = 0
        while l<r:
            if heights[l] > heights[r]:
                area = heights[r] * (r-l)
                maxarea = max(maxarea, area)
                r -= 1
            elif heights[l] < heights[r]:
                area = heights[l] * (r-l)
                maxarea = max(maxarea, area)
                l += 1
            else:
                area = heights[l] * (r-l)
                maxarea = max(maxarea, area)
                l += 1
                r -= 1
        return maxarea
                

        