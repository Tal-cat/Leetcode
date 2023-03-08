'''
Level: easy
Performance: Runtime 35ms, Beats 63.71%, Memory 13.8MB, Beats 51.85. 
'''

# del() and pop() would change index, geberating error in itteration.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
