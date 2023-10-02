n = int(input("Enter the size of the matrix: "))
matrix = [[0 for j in range(n)] for i in range(n)]
start_row, end_row = 0, n-1
start_col, end_col = 0, n-1
count = 1
while start_row <= end_row and start_col <= end_col:
    for i in range(start_col, end_col+1):
        matrix[start_row][i] = count
        count += 1
    for i in range(start_row+1, end_row+1):
        matrix[i][end_col] = count
        count += 1   
    for i in range(end_col-1, start_col-1, -1):
        matrix[end_row][i] = count
        count += 1 
    for i in range(end_row-1, start_row, -1):
        matrix[i][start_col] = count
        count += 1
    start_row += 1
    end_row -= 1
    start_col += 1
    end_col -= 1
for i in range(n):
    for j in range(n):
        print("{:2d}".format(matrix[i][j]), end=" ")
    print()