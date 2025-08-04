class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left = 1
        right = 1

        for i in range(n):
            answer[i] *= left
            left *= nums[i]

            answer[n - 1 - i] *= right
            right *= nums[n - 1 - i]

        return answer
            
