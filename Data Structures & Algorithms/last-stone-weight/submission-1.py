class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        new = [0]*n
        for x in range(n):
            new[x] = -stones[x]
        heapq.heapify(new)

        while len(new)>1:
            large1 = -heapq.heappop(new)
            large2 = -heapq.heappop(new)
            diff = large1-large2
            if diff!=0:
                heapq.heappush(new,(-diff))
        if new:
            res = -new[0]
            return res
        else:
            return 0
            
