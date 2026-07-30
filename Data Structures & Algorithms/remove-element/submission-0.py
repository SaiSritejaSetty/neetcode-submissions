class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for y in range(len(nums)):
            if nums[y] != val:
                nums[x] = nums[y]
                
                x += 1
                
        return x
        