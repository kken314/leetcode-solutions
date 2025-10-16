class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        def fibo(n):
            if dp[n] != -1:
                return dp[n]
            dp[n] = fibo(n - 1) + fibo(n - 2) 
            return dp[n]
        return fibo(n)