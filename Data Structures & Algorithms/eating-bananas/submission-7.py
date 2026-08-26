class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l = 1
        r = max(piles)
        res = None
        while l < r:
            mid = (l+r)//2
            hrs = 0
            for p in piles:
                hrs+=math.ceil(float(p)/mid)
            if hrs <= h:
                res = mid
                r = mid
            else:
                l = mid+1
        return l

        
                        
            
            

        