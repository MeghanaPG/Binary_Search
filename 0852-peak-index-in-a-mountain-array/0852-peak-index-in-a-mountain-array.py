class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = l + (r-l)//2
            
            if arr[mid] > arr[mid + 1]:
                # we are in the decreasing part of the array so move left
                r = mid
            else:
                # we are in the increasing part of the array so move right 
                l = mid + 1 
        return l