import sys
input = sys.stdin.readline

sudoku = [list(map(int,input().split())) for _ in range(9)]
queue = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            queue.append((i,j))

def check(x,y,i):
    for j in range(9):
        if sudoku[x][j]==i:
            return False
    for j in range(9):
        if sudoku[j][y]==i:
            return False
    for j in range(3):
        for k in range(3):
            if sudoku[x//3*3+j][y//3*3+k]==i:
                return False
    return True
    

def backtracking(num):
    if num==len(queue) :
        for i in sudoku:
            print(*i)
        exit()
    for i in range(1,10):
        x, y=queue[num]
        if check(x,y,i):
            sudoku[x][y]=i
            backtracking(num+1)
            sudoku[x][y]=0
backtracking(0)