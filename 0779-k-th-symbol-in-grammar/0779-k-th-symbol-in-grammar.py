class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Time Complexity: O(n)
        # 0
        #0 1
        ######
        # 1
        #1 0
        
        cur = 0 
        left, right = 1, 2 ** (n-1)

        for _ in range(n-1):
            mid = (left + right)//2
            if k <= mid:
                right = mid 
            else:
                left = mid + 1
                cur = 0 if cur else 1 

        return cur 
        
