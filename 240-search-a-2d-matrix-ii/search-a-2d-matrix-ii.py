class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        #if the rows and cols are sorted inherit that the top right element consideration
        row = 0
        col = cols - 1
        while(row<rows and col>=0):
            current = matrix[row][col]
            if current > target:
                col -= 1
            if current == target:
                return True
            elif current < target:
                row += 1
        return False
