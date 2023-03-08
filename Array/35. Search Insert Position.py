'''
Level: easy
Performance: Runtime 54ms, Beats 51.6%, Memory 14.6MB, Beats 72.6%. 
'''

# DO consider all possible comparison resluts.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # START
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        if target not in nums:
            for j in range(len(nums)):
                if nums[-1] < target:
                    return len(nums)
                
                if nums[0] > target:
                    return 0

                if nums[j] < target and nums[j+1] > target:
                    return j+1

