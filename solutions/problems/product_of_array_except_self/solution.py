class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        leftproduct = 1
        for i in range(len(nums)):
            result[i] = leftproduct
            leftproduct *= nums[i]
        rightproduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= rightproduct
            rightproduct *= nums[i]
        return result