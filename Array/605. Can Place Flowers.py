class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # START
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            # Both sides shall be 0 or at either the start or the end of flowerbed
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                
        if n <= 0:
            return True

        return False
