class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # START
        # UNDERSTAND the calculation is the most important part
        if 0 not in nums:
            return 0
        
        cur = 0
        total = 0
        for i in nums:
            if i == 0:
                cur += 1
                total += cur
            else:
                cur = 0
        
        return total
