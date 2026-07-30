class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        l = 0
        r = len(nums1)
        half = (len(nums1)+len(nums2)+1)//2
        
        
        while l <= r:
            i = (r+l)//2
            j = half - i
            Aleft = nums1[i-1] if i>0 else  float("-inf")
            Aright = nums1[i] if i<len(nums1) else float("inf")
            Bleft = nums2[j-1] if j> 0 else float("-inf")
            Bright = nums2[j] if j<len(nums2) else float("inf")
            if Aleft<=Bright and Aright>=Bleft:
                break
            elif Aleft>Bright:
                r= i-1
            elif Aright<Bleft:
                l = i+1
        if (len(nums1)+len(nums2))%2 != 0:
            return max(Aleft,Bleft)
        elif (len(nums1)+len(nums2))%2 == 0:
            return (max(Aleft,Bleft) + min(Bright,Aright))/2
            