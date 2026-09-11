def rowWithMax1s(mat):
    rows = len(mat)
    cols = len(mat[0])

    max_ones = 0
    max_row = -1

    for row in range(rows):
        low = 0
        high = cols - 1

        while low <= high:
            mid = (low + high) // 2

            if mat[row][mid] <= 0:
                low = mid + 1
            else:
                high = mid - 1

        ones = cols - low

        if ones > max_ones:
            max_ones = ones
            max_row = row

    return max_row


# Manual input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

answer = rowWithMax1s(matrix)

print("Row with maximum 1s:", answer)