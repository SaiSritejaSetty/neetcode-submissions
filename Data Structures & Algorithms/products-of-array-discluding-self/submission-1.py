class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n

        product_left = 1
        for i in range(n):
            result[i] = product_left
            product_left *= nums[i]

        product_right = 1
        for j in range(n-1, -1, -1):
            result[j] *= product_right
            product_right *= nums[j]

        return result