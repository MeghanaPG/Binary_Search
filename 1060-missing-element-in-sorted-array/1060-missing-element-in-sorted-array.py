class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Time: O(logn)
        # Binary Search 
        l, r = 0, len(nums) - 1

        # return number of missing #s at index i
        missing = lambda i: nums[i] - nums[0] - i

        # edge case where the missing number is past the last number 
        if k > missing(r):
            return nums[r] - missing(r) + k 

        # binary search 
        while l + 1 < r:
            m = (l + r) // 2
            x = missing(m)
            if k <= x:
                r = m 
            else:
                l = m
        return nums[l] - missing(l) + k 