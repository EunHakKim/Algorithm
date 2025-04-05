n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def back(index):
    global ans
    if index == n:
        ans = max(ans, sum(1 for s, _ in eggs if s <= 0))
        return

    if eggs[index][0] <= 0:
        back(index + 1)
        return

    is_hit = False
    for i in range(n):
        if i == index or eggs[i][0] <= 0:
            continue
        is_hit = True

        # 저장
        eggs[index][0] -= eggs[i][1]
        eggs[i][0] -= eggs[index][1]

        back(index + 1)

        # 복구
        eggs[index][0] += eggs[i][1]
        eggs[i][0] += eggs[index][1]

    if not is_hit:
        back(index + 1)

back(0)
print(ans)