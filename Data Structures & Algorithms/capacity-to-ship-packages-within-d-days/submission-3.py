class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        mini = 0
        while l <= r:
            day = 1
            mid = (l+r) // 2
            load = 0
            for x in weights:
                if load + x > mid:
                    load = 0
                    day += 1
                load += x
            if day <= days:
                r = mid - 1
                mini = mid
            elif day > days:
                l = mid + 1
        return mini                
                    
                
        