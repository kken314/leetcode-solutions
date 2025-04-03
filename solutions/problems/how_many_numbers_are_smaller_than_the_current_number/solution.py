class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Map = {}
        nums_sort = sorted(nums)
        for i in range(len(nums)):
            if nums_sort[i] not in Map:
                Map[nums_sort[i]] = i
        for i in range(len(nums)):
            nums[i] = Map[nums[i]]
        return nums
        