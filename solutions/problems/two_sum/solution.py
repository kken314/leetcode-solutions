class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # key is number , value is index
        for i in range(len(nums)):
            find = target - nums[i]
            if find in dic:
                return dic[find], i
            dic[nums[i]] = i
