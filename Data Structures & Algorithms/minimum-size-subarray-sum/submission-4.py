class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current = 0
        best = float("inf") 
        l = 0 
        for r in range(len(nums)):
            current += nums[r]
            while current >= target:
                best = min(best,r-l+1)
                current -= nums[l]
                l+=1
        if best != float("inf"):
            return best
        else:
            return 0
