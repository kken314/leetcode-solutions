class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_count = 0
        if n == 0:return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                empty_count += 1
                flowerbed[i] = 1
        return n <= empty_count