class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        number_1 =None
        number_2 = None 
        count_1 =0
        count_2 = 0
        res = []
        for x in nums:
            if x == number_1:
                count_1+=1
            elif x == number_2:
                count_2+=1
            elif count_1 == 0:
                number_1 = x
                count_1 = 1
            elif count_2 ==0:
                number_2= x
                count_2 = 1
            else:
                count_1 -= 1
                count_2-=1
        count_1 = count_2 = 0
        for x in nums:
            if x == number_1:
                count_1 +=1
            elif x==number_2:
                count_2+=1
        if count_1 > n//3:
            res.append(number_1)
        if count_2 > n//3:
            res.append(number_2)

        return res