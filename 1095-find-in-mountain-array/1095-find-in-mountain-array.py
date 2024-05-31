# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Time Complexity: O(logn)
        # Binary Search 

        length = mountain_arr.length()

        # Find peak
        # As we know that the peak is not gonna be at the edges 
        l, r = 1, length - 2 
        while l <= r:
            m = (l + r) // 2 
            left, mid, right = mountain_arr.get(m-1), mountain_arr.get(m), mountain_arr.get(m+1)
            if left<mid<right:
                l = m + 1 
            elif left>mid>right:
                r = m - 1 
            else:
                break
        peak = m 

        # We are searching for the target value 
        # Search left portion 
        l, r = 0, peak
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1 
            elif val > target:
                r = m - 1 
            else:
                return m 

        # Search left portion 
        l, r = peak, length - 1 
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val > target:
                l = m + 1 
            elif val < target:
                r = m - 1 
            else:
                return m 
        return -1