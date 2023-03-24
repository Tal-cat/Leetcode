class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # START
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = left + (right - left)//2 # 整除

            if nums[middle] > target:
                right = middle - 1
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] == target:
                return middle
        
        return -1
