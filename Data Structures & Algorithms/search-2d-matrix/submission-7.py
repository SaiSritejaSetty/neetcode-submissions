class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        columns = len(matrix[0])
        row = len(matrix)
        r = row * columns - 1
        while l <= r:
            mid = (l+r) // 2
            RO = mid// columns
            CO = mid % columns
            if matrix[RO][CO] == target:
                return True
            elif matrix[RO][CO] > target:
                r = mid - 1
            elif matrix[RO][CO] < target:
                l = mid + 1
        return False
