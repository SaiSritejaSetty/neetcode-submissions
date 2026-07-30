class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 0
        l = 1
        r = max(piles)
        while l <= r:
            k = (r+l)//2
            hrs=0
            for p in piles:
                hrs += math.ceil(float(p)/k)
            if hrs <= h:
                mini = k
                r = k -1
            else:
                l = k+1
        return mini
            
                        
            
            

        