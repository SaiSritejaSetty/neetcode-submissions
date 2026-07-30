class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_output = float("inf")
        output = 0
        l = 0
        for x in range(len(nums)):
            output += nums[x]
            while output >= target:
                best_output= min(x-l+1, best_output)
                output -= nums[l]
                l+=1
        return best_output if best_output != float("inf") else 0
            
                    
