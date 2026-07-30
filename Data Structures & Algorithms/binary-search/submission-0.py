class Solution:
    def search(self, nums: List[int], target: int) -> int:
      for x in range(len(nums)):
        if nums[x] == target:
          return x
        elif nums[x] != target:
          pass
      return -1        