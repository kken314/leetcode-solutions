class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect_sum = int((n*(n+1))/2)
        sum = 0
        for num in nums:
            sum += num
        return expect_sum - sum