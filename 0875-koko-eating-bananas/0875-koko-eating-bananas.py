class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_no_bananas = max(piles)
        left, right = 1, max_no_bananas
        k = max_no_bananas

        while left <= right:
            mid = left + (right - left)//2
            hours = 0 
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1 
                k = min(k, mid)
        return k 