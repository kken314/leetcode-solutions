class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            find = target - nums[i]
            if find in dic:
                return [dic[find], i]
            dic[nums[i]] = i