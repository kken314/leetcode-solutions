class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxval = 0
        for num in num_set:
            if num - 1 not in num_set:
                lenght = 0
                while num + lenght in num_set:
                    lenght += 1
                maxval = max(maxval, lenght)
        return maxval