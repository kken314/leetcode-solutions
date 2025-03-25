class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index1 = 0
        index2 = len(nums) - 1
        while index1 <= index2:
            mid = index1 + (index2 - index1)//2
            if nums[mid] == target:
                return mid
            elif(target < nums[mid]):
                index2 = mid - 1
            elif(target > nums[mid]):
                index1 = mid + 1 
        return -1