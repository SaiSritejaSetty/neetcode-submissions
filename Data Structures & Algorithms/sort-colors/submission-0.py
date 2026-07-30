class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(len(nums)):
            for j in range(x+1,len(nums)):
                if nums[x] > nums[j]:
                    nums[x],nums[j] = nums[j],nums[x]
                    
        