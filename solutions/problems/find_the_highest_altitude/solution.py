class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for g in gain:
            altitudes.append(altitudes[-1] + g)
        return max(altitudes)