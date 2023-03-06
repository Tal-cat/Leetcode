'''
Performance
Runtime 7335ms, Beats 6.33%, Memory 14.9MB, Beats 91.41. 
'''

'''
Instead of comparing values , index comparasion shall be used since there exists duplicate values.

Function enumernate() can reture both index and item in given lists. So we don't need to define an i or j 
to keep track of the index.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, item_1 in enumerate(nums):
            for index_2, item_2 in enumerate(nums):
                if index_1 !=  index_2:
                    if target == item_1 + item_2:
                        return([index_1, index_2])
