import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
queens = []
ans = 0

def back():
    global ans
    if len(queens) == n:
        ans += 1
        return

    for i in range(n):
        if i not in queens:
            if chk(i):
                queens.append(i)
                back()
                queens.pop()

def chk(temp):
    top = temp
    bottom = temp
    i = len(queens) - 1
    while i >= 0:
        top -= 1
        bottom += 1
        if queens[i] == top or queens[i] == bottom:
            return False
        i -= 1
    return True

back()
print(ans)