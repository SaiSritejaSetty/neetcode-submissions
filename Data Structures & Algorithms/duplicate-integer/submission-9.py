class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      hashed = []
      for x in nums:
        if x in hashed:
            return True
        else:
            hashed.append(x)
      return False