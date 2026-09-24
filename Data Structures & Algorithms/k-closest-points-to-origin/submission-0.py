class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ret = []
        n = len(points)
        for x in points:
            i = x[0]
            j = x[1]
            diff = ((i-0)**2) + ((j-0)**2)
            res.append([diff,x])
        heapq.heapify(res)
        for _ in range(k):
            l = heapq.heappop(res)
            ret.append(l[1])
        return ret

    
        

        
        