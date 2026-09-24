class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = []
        for x in nums:
            new.append(-x)
        heapq.heapify(new)

        for _ in range(k):
            res = heapq.heappop(new)
        return -res

        
        