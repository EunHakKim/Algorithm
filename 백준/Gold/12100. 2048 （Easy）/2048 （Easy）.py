import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 0: 좌, 1: 하, 2: 우, 3: 상
# 보드 이동
def move(b, k):
    is_plus = [[False] * n for _ in range(n)]
    # k만큼 회전 필요
    new_b = [[0] * n for _ in range(n)]
    return_b = [[0] * n for _ in range(n)]
    if k == 0:
        for i in range(n):
            for j in range(n):
                new_b[i][j] = b[i][j]
    elif k == 1:
        for i in range(n):
            for j in range(n):
                new_b[j][n - 1 - i] = b[i][j]
    elif k == 2:
        for i in range(n):
            for j in range(n):
                new_b[n - 1 - i][n - 1 - j] = b[i][j]
    else:
        for i in range(n):
            for j in range(n):
                new_b[n - 1 - j][i] = b[i][j]

    # 이동(좌로 이동을 기준)
    for i in range(1, n):
        for y in range(n):
            j = i
            while j >= 1:
                # 0일때
                if new_b[y][j] == 0:
                    break
                # 왼쪽이 비어있을 때 이동
                elif new_b[y][j - 1] == 0:
                    new_b[y][j - 1] = new_b[y][j]
                    new_b[y][j] = 0
                    is_plus[y][j - 1] = is_plus[y][j]
                    is_plus[y][j] = False
                # 왼쪽이 같은 수일 때
                elif new_b[y][j - 1] == new_b[y][j]:
                    # 두 수중 하나가 이미 더해졌다면
                    if is_plus[y][j - 1] or is_plus[y][j]:
                        break
                    new_b[y][j - 1] *= 2
                    new_b[y][j] = 0
                    is_plus[y][j - 1] = True
                    is_plus[y][j] = False
                # 왼쪽이 다른 수일 때
                elif new_b[y][j - 1] != new_b[y][j]:
                    break
                j -= 1

    # 다시 회전 필요
    if k == 0:
        for i in range(n):
            for j in range(n):
                return_b[i][j] = new_b[i][j]
    elif k == 1:
        for i in range(n):
            for j in range(n):
                return_b[n - 1 - j][i] = new_b[i][j]
    elif k == 2:
        for i in range(n):
            for j in range(n):
                return_b[n - 1 - i][n - 1 - j] = new_b[i][j]
    else:
        for i in range(n):
            for j in range(n):
                return_b[j][n - 1 - i] = new_b[i][j]

    return return_b

# 백트래킹
def back(b, depth):
    global ans
    if depth == 5:
        for x in b:
            temp = max(x)
            ans = max(ans, temp)
        return

    for k in range(4):
        back(move(b, k), depth + 1)

back(board, 0)
print(ans)