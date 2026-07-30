class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        n = len(nums)*2
        ans = [0] *n
        for i in range(0,x):
            ans[i] = nums[i]
            ans[i+x] = nums[i]
        return ans




        