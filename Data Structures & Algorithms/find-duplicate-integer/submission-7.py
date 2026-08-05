class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low = 1
        high = n
        while low<high:
            mid = (low+high)//2
            count = 0
            for x in nums:
                if x <= mid:
                    count+=1
                else:
                    pass
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
                
            