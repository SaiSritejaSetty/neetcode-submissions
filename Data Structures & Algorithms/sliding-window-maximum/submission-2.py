class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = deque()
        res = []
        for r in range(len(nums)):
            while curr and nums[r] > nums[curr[-1]]:
                curr.pop()
            curr.append(r)
            if curr[0] < r-k+1:
                curr.popleft()
            if r >= k -1:
                res.append(nums[curr[0]])
        return res

            


        
        