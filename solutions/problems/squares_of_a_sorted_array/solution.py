class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums)-1
        list = []
        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                list.append(nums[p1]**2)
                p1+=1
            else:
                list.append(nums[p2]**2)
                p2-=1
        list.reverse()
        return list