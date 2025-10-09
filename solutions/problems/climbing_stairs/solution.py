class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(k):
            if k < 0:
                return 0
            elif k == 0:
                return 1
            if k in memo:
                return memo[k]
            
            memo[k] = climb(k - 1) + climb(k - 2)
            return memo[k]
        
        return climb(n)