class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # START
        mergedArray = []
        totalLen = len(nums1) + len(nums2)
        for i in range(len(nums1)):
            mergedArray.append(nums1[i])

        for j in range(len(nums2)):
            mergedArray.append(nums2[j])

        mergedArray.sort()
        
        if len(mergedArray)%2 == 0:
            return (mergedArray[int(totalLen/2 - 1)] + mergedArray[int(totalLen/2)])/2
        else:
            return mergedArray[int((totalLen-1)/2)]
