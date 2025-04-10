class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p1] == 0 and nums[p2] != 0:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                p1 += 1
                p2 += 1
            elif nums[p1] != 0 and nums[p2] == 0:
                p1 += 1
                p2 += 1
            elif nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            else:
                p1 += 2
                p2 += 2
