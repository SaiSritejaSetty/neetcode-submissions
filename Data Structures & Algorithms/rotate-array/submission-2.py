class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l =0
        r = len(nums)-1
        k = k % len(nums)
        n = len(nums)
        while l<r:
            nums[l],nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        l=0
        r=len(nums)-1
        k_2 = k-1
        k_3 = k
        while l<k_2:
            nums[l],nums[k_2]=nums[k_2],nums[l]
            l+=1
            k_2-=1
        while r>k_3:
            nums[r],nums[k_3]=nums[k_3],nums[r]
            r-=1
            k_3+=1
        