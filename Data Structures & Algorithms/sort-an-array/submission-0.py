class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] > nums[y]:
                    nums[x],nums[y] = nums[y],nums[x]
        return nums



        