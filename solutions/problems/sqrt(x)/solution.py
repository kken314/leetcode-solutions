class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        res = 0
        while L <= R:
            mid = (L + R) // 2
            if mid * mid < x:
                L = mid + 1
                res = mid
            elif mid * mid > x:
                R = mid - 1
            else:
                return mid
        return res