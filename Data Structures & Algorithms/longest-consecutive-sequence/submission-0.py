class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        seq = 0
        for i in n:
            if i-1 not in n:
                current = 1
                while i+current in n:
                    current +=1
                seq = max(current, seq)
        return seq


