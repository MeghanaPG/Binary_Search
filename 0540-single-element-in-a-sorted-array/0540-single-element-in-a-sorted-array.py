class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Time Complexity: O(log n)
        # Binary Search 

        l, r = 0, len(nums) - 1 

        while l <= r:
            m = l + ((r-l)//2)

            # if a number has both different neighbors then it is the element which appears 
            # only once in the array 
            # bcz the first element doesn't have a neighbor 
            if((m-1<0 or nums[m-1]!= nums[m]) and (m+1 == len(nums) or nums[m] != nums[m+1])):
                return nums[m]

            #if not the above condition, we have to figure out which side of the array has
            #odd number of elements, as that side will have the single element 
            leftSize = m - 1 if nums[m-1] == nums[m] else m 

            # Odd number on the left side 
            if leftSize % 2:
                r = m - 1 
            else:
                l = m + 1 
                