import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        nums = nums1 + nums2 
        nums.sort() 
        l=len(nums)
        if(l%2==0):
            i=int(l/2)
            print(i)
            med=(nums[i]+nums[(i)-1])/2
        else:
            i=int(l/2)
            med=nums[i]
        return med
           
        