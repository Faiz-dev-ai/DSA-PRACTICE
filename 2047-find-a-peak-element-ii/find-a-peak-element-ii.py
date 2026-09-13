class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        low = 0
        high = cols-1
        while(low<=high):
            mid_col = (low + high)//2
            #now we need to find the bigger element in the column and note its index values
            max_value = -float('inf')
            max_row = 0
            for row in range(rows):
                current = mat[row][mid_col]
                if current > max_value:
                    max_value = current
                    max_row = row 
            #edge cases
            left = mat[max_row][mid_col-1] if mid_col != 0 else -float('inf')
            right = mat[max_row][mid_col+1] if mid_col < cols -1 else -float('inf')
            if max_value > left and max_value > right:
                return [max_row,mid_col]
            elif left > max_value:
                high = mid_col - 1
            else:
                low = mid_col + 1
                
            
        