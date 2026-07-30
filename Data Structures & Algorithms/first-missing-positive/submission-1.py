class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set()
        num=1
        for x in nums:
            if x>0:
                s.add(x)
        while num in s:
            num+=1
        return num
        
                