class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for x in range(0,len(nums)-1):
            for j in range(x+1, len(nums)):
                if nums[x]==nums[j] and abs(x-j)<=k:
                    return True
        return False 
