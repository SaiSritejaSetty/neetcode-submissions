class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        for x in range(len(heights)):
            l = x-1
            r = x+1
            width = 1
            while l > -1:
                if heights[x] <= heights[l]:
                    l-=1
                    width +=1
                elif heights[x] > heights[l]:
                    break
            while r < len(heights):
                if heights[x] <= heights[r]:
                    r+=1
                    width +=1
                elif heights[x] > heights[r]:
                    break
            stack.append(width * heights[x])
        maximum = max(stack)
        return maximum 

                
        