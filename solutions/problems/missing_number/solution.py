class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        # if nums in already sorted
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left