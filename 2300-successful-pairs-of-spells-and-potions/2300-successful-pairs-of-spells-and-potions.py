class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Time Complexity: n + m (logm)
        # we are trying to see the min value that will work 
        potions.sort()
        res = [] 

        for s in spells:
            l, r = 0, len(potions) - 1 
             # find the weakest potion (furthest left) that works 
             # so basically the rest of the values will satisy the condition 
            idx = len(potions)

            while l <= r:
                m = l + ((r-l)//2)
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m 
                else:
                    l = m + 1 

            res.append(len(potions) - idx)
        return res 



            
        # we will have to reset the count to make sure we are able 
        # to use it for other spells as well