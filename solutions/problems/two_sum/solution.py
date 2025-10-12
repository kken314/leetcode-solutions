class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumToIndex = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in NumToIndex:
                return [i, NumToIndex[find]]
            NumToIndex[nums[i]] = i
