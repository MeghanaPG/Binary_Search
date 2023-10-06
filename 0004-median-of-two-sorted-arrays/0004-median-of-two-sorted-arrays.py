class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1 + nums2 
        nums.sort() 
        left, right = 0, len(nums)-1 

        while left <= right:
            mid = left + (right - left) // 2 
            if len(nums) % 2 != 0:
                return nums[mid]
            
            if len(nums) % 2 == 0:
                k = nums[mid]
                right = mid + 1 
                num = nums[right]
                calc = (k+num)/2
                return calc



