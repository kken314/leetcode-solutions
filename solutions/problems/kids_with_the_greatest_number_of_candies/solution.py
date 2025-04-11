class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxkid = max(candies)
        result = []
        for kid in candies:
            result.append(kid + extraCandies >= maxkid)
        return result