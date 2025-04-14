class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left,right):
            if left > right:
                return left
            mid = (right + left) // 2
            if target > nums[mid]:
                 return binarySearch(mid + 1, right)
            elif target < nums[mid]:
                 return binarySearch(left, mid - 1)
            else:return mid

        return binarySearch(0, len(nums) - 1)