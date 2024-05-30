class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n.logS) [S is the sum of the input arrays]
        # Min our res could be is max(nums)
        # MAx our res could be is min(nums)
        def canSplit(largest):
            subarray = 0 
            curSum = 0 
            for n in nums:
                curSum += n 
                if curSum > largest:
                    subarray += 1 
                    curSum = n 
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            mid = l + ((r-l) // 2)
            if canSplit(mid):
                res = mid 
                r = mid - 1 
            else:
                l = mid + 1 
        return res 
       

