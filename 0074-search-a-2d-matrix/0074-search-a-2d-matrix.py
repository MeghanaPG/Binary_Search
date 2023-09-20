class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0 
        j = 0 
        num_rows = len(matrix)
        
        while i < num_rows:
            # Checking one row at a time
            if matrix[i][0]<= target <=matrix[i][-1]:
                left, right = 0, len(matrix[0])-1
                while left <= right:
                    mid = left + (right- left) // 2 
                    if matrix[i][mid] == target:
                        return True 
                    if target < matrix[i][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1 
                return False  
                # Linear Search 
                # for j in range(len(matrix[0])):
                #     if matrix[i][j] == target:
                #         return True 
                # return False 
            i += 1
        
        return False


                    

        