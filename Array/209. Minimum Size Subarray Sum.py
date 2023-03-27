class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # START
        sum = 0
        length = 0
        start = 0 
        res = float('inf') # define a large value for initialization
        for j in range(len(nums)):
            sum += nums[j]
            while (sum >= target):
                length = j - start + 1
                res = min(length, res)
                sum -= nums[start]
                start += 1

        if res == inf:
            return 0
        
        return res
