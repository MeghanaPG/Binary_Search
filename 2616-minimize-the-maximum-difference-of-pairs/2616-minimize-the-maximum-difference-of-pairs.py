class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Time Complexity: 
        # We will not have more than n/2 pairs 
        # The goal is to get a difference which is min as possible 
        # We are not running Binary Search on arr
        def isValid(threshold):
            #Greedy 
            i, cnt = 0, 0 
            while i < len(nums) - 1:
                if (abs(nums[i]- nums[i+1])) <= threshold:
                    cnt += 1 
                    # 2 because we have used both the values and can't use them again.
                    i += 2 
                else:
                    i += 1 
                if cnt == p:
                    return True 
            return False

        if p == 0: return 0 
        
        nums.sort()
        l, r = 0, 10**9
        res = 10**9

        while l<=r:
            m = l + (r-l)//2
            if isValid(m):
                res = m
                r = m - 1 
            else:
                l = m + 1
        return res 