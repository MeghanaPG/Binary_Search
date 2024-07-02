class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  Time Complexity: O(m+n)
        # Binary Search 
        # Instead of row wise search we will have to do column wise search
        n, m = len(matrix), len(matrix[0])

        r, c = n-1, 0 

        while r >= 0 and c <m:
            if matrix[r][c] == target:
                return True 
            if matrix[r][c] > target:
                r -= 1 
            else:
                c += 1 
        return False 