class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        Alsum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                Alsum += nums[i]
            else:
                Alsum -= nums[i]
        return Alsum