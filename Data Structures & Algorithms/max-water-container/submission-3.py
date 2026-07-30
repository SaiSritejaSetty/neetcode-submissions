class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l= 0
        r=len(heights)-1
        width = 0
        height = 0
        results = 0
        while l<r:
            height = min(heights[r],heights[l])
            width = r - l
            current = width * height
            results= max(results,current)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1   
        return results 



