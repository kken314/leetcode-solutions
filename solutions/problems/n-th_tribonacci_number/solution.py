class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        dp = [-1] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        def tribo(n):
            if dp[n] != -1:
                return dp[n]
            dp[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)
            return dp[n]
        return tribo(n)