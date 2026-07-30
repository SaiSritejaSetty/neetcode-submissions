class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in range(1,len(nums)):
            if nums[x] != nums[k]:
                k +=1 
                nums[k] = nums[x]
        return k + 1