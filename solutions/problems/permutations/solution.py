class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        allPermutations = []
        currPermutation = []
        isUsed = [False] * n

        def backtrack():
            if len(currPermutation) == n:
                allPermutations.append(currPermutation[:])
                return

            for i, num in enumerate(nums):
                if not isUsed[i]:
                    currPermutation.append(num)
                    isUsed[i] = True
                    backtrack()
                    currPermutation.pop()
                    isUsed[i] = False

        backtrack()
        return allPermutations