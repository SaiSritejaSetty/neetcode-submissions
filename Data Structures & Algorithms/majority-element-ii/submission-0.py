class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = []
        majority_dict = {}
        n = len(nums)
        for x in nums:
            if x in majority_dict:
                majority_dict[x] +=1
            else:
                majority_dict[x] = 1
        for key in majority_dict:
            if majority_dict[key] > n/3:
                majority.append(key)
        return majority
              