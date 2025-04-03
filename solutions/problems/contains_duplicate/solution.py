class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            if num in set1:
                return True
            set1.add(num)
        return False