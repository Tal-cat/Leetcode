'''
Level: medium
Performance: Runtime 769ms, Beats 61.66%, Memory 27.4MB, Beats 84.53%. 
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # START
        '''
        # Time Limit Exceeded
        # double iteration costs to much
        v = 0
        for i in range(0,len(height)): # the second last
            for j in range (i+1, len(height)):
                v = max(v, (j-i)* min(height[i], height[j]))
        return v
        '''

        v = 0
        l = 0 
        r = len(height) - 1
        while l < r:
            v = max(v, (r-l)* min(height[r], height[l])) 
            # move the lower on for max area
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return v
