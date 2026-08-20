class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        width = 0
        height = 0
        current = 0
        while l < r:
            width = r - l
            height = min(heights[r],heights[l])
            current = height * width
            res = max(current,res)
            if heights[r] >= heights[l]:
                l+=1
            else:
                r-=1
        return res
            




