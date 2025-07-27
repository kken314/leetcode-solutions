class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # key is number , value is index
        for i, num in enumerate(nums):
            find = target - num
            if find in dic:
                return dic[find], i
            dic[num] = i
