class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = {}
        for x in nums:
            if x in l:
                l[x] += 1
            else:
                l[x] = 1
        for key in l:
            if l[key] > len(nums)/2:
                return key
        

        