class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxcount = 2
        for i in range(len(nums) - 2):
            count = 2
            j = i
            while nums[j] + nums[j+1] == nums[j+2] and j + 2 < len(nums):
                count += 1
                j += 1
                if j + 2 >= len(nums):
                    break
            maxcount = max(maxcount, count)
        return maxcount