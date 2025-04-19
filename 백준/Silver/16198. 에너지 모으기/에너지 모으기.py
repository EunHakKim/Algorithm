import sys
input = sys.stdin.readline

n = int(input())
energy = list(map(int, input().split()))
ans = 0

def back(cnt):
    global ans
    if len(energy) == 2:
        ans = max(ans, cnt)
        return

    for i in range(1, len(energy) - 1):
        to_add = energy[i - 1] * energy[i + 1]
        temp = energy.pop(i)
        back(cnt + to_add)
        energy.insert(i, temp)

back(0)
print(ans)