'''
Level: easy
Performance: Runtime 9918ms, Beats 5%, Memory 18.2MB, Beats 74.26%. 
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # START 
        '''
        Time Limit Exceeded
        
        Too many for loops.

        if len(nums) < 3:
            return []

        sum = []
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = sorted([nums[i] ,nums[j] ,nums[k]])
                        if a not in sum:
                            sum.append(a)
        return sum
        '''
        
        if len(nums) < 3:
            return []


        results = []
        # smallest to largest
        nums.sort()

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    sum = sorted([nums[i], nums[left], nums[right]])
                    if sum not in results:
                        results.append(sum)
                    left = left + 1
                    right = right - 1
            
                elif nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
            
                else:
                    right = right - 1

        return results
