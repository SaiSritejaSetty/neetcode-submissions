class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        g = {}
        for i in range(len(nums)):
                difference = target - nums[i]
                if difference not in g:
                    g[nums[i]] = i
                elif difference in g:
                        return [g[difference], i]
                
            
