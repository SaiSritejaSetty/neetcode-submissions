class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        number = None 
        for x in nums:
            if count == 0:
                number = x
            if number == x:
                count += 1
            if number != x:
                count-=1
        return number 

        