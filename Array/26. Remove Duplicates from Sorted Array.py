'''
Level: easy
Performance: Runtime 88ms, Beats 73.38%, Memory 15.5MB, Beats 51.11%. 
'''

'''
Two points are need. One to keep track of current elements. Another to keep track of non-duplicate elements.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l = l + 1
        return l
