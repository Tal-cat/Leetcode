class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # START
        '''
        # Time Limit Exceeded
        nums.sort()
        Length = len(nums)
        if Length == 1:
            if nums[0] != 1:
                return 1
            else:
                return 2
        for i in range(1, Length+2): # range [)）
            if i not in nums:
                return i
        '''
        length = len(nums)
        for i in range(length):
            correctPosition = nums[i] - 1
            while 1 <= nums[i] <= length and nums[i] != nums[correctPosition]:
                nums[i], nums[correctPosition] = nums[correctPosition], nums[i]
                correctPosition = nums[i]-1
        '''
        Suppose [10,9,8,7,6,3]
        length = 6
        10, 9, 8, 7 > length
        For 6 (i = 4):
            1 <= 6 <= 6 and nums[4](6) != nums[5](3) √
            After change:
            nums[4] = 3, nums[5] = 6(correct)
            correctPosition = nums[4](now is 3) - 1 = 2
            Note: i is still 4, so the loop continues
            1 <= 3 <= 6 and nums[4](3) != nums[2](8) √
            After change:
            nums[4] = 8, nums[2] = 3(correct)
            Note 8 is out of range now, exist.
            Final:
            [10,9,3,7,8,6]

        '''

        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1
        
        return length + 1
