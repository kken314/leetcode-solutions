class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            res = pow(x, n // 2)
            res = res * res
            if n % 2 == 1:
                res *= x
            return res
        res = pow(x, abs(n))
        if n < 0:
            return 1 / res
        else:
            return res