class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = 0
        while l <= r:
            mid = (l+r) // 2
            f = 1
            load = 0
            for x in nums:
                if x + load > mid:
                    load = 0
                    f+=1
                load += x
            if f <= k:
                r = mid-1 
                res = mid
            else:
                l = mid + 1
        return res  
            