

def valid(row, col, grid, n):

    for c1 in range(0, n):
        if grid[row][c1] == 1:
            return False

    for r1 in range(0, n):
        if grid[r1][col] == 1:
            return False
    for i in range(0,  n):
        if (row+i) >= n or (col + i) >= n:
            continue
        if grid[row + i][col + i] == 1:
            return False
    for i in range (0,n):
        if (row-i) < 0 or (col-i) < 0:
            continue
        if grid[row - i][col - i] == 1:
            return False
    for i in range(0,n):
        if (row + i) >= n or (col - i) < 0:
            continue
        if grid[row + i][col - i] == 1:
            return False
    for i in range(0,n):
        if (row - i) < 0 or(col + i) >= n:
            continue
        if grid[row - i][col + i] == 1:
            return False
    return True


grid = [[0, 0, 0, 1,0,0,0,0],
        [0, 0, 0, 0,0,0,0,0],
        [0, 0, 0, 0,1,0,0,0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0,0,0,0,0]]


def queens(n, col):
    # global grid
    if col >= n:
        return True
    for row in range(0, n):
        v = valid(row, col, grid, n)
        if v == True:
            grid[row][col] = 1 # Temp
            if queens(n, col + 1):
                return True
            grid[row][col] = 0  

    return False


N = 10
col = 8
ans =  queens(N, col)
for i in range (0, N):
    new = []
    for j in range (0,N):
        new.append(0)
    grid.append(new)

