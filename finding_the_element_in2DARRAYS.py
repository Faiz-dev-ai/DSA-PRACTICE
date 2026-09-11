def findingelement(matrix,target,rows,cols):
    low = 0 
    high = (rows*cols-1)
    while(low<=high):
        mid = (low + high)//2
        #convert flattened mid into the matrix row and cols
        row = mid//cols
        col = mid % cols
        if matrix[row][col] == target:
            return row,col
        elif matrix[row][col]<target:
            low = mid + 1
        else:
            high = mid - 1
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = 3
cols = 3
target = 8
print(findingelement(matrix,target,rows,cols))
