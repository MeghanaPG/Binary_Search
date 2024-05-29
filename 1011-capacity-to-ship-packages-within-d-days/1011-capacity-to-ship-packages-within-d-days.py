class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Time Complexity: O(n.logm)
        # Binary Search 
        # Capacity -> Lower bound is the max weight and upper bound will 
        # be the sum of weights of input array
        # The goal is to minimize the capacity 

        l, r = max(weights), sum(weights)
        res = r 

        def canShip(cap):
            ships, currCap = 1, cap 

            for w in weights:
                # currCap can't hold the weight
                if currCap - w < 0:
                    ships += 1 
                    currCap = cap
                # if the currCap can hold the weight then we substract the w from currCap
                currCap -= w
            return ships <= days 

        while l <= r:
            cap = l + (r-l)//2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1 
        return res
