class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = 0
        r = len(nums)-1
        n = len(nums)
        k = k % n
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            r-=1
            l+=1
        l = 0
        r= k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            r-=1
            l+=1
        l = k
        r = len(nums)-1
        while l <r:
            nums[l],nums[r] = nums[r],nums[l]
            r-=1
            l+=1

    

        """
        Do not return anything, modify nums in-place instead.
        """
               