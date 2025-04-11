class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 < p2:
            volume = (p2 - p1) * (min(height[p1],height[p2]))
            maxVolume = max(volume, maxVolume)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxVolume