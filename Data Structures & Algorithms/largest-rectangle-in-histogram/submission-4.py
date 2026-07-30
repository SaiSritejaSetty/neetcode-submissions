class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        for x in range(len(heights)):
            while stack and heights[stack[-1]] > heights[x]:
                h = heights[stack.pop()]
                if stack:
                    width = x - stack[-1] - 1
                else:
                    width = x
                area = max(area, h * width)

            stack.append(x)
        return area
            
                
        