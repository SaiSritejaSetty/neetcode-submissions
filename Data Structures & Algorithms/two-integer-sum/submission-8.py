class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in hashed:
                return [hashed[diff], x]
            else:
                hashed[nums[x]] = x        
            
