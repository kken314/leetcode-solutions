class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            SumSq = 0
            while n != 0:
                SumSq += (n % 10) ** 2
                n //= 10
            n = SumSq
        return n == 1