class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        round_off = 0
        while l <= r:
            mid = (r+l) // 2
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                r = mid - 1
            elif mid*mid < x:
                l = mid + 1
                round_off = mid

        return int(round_off)