import sys
input = sys.stdin.readline

n = int(input())
prime = []
y, cnt, ans = -1, 0, 0

def check_prime():
    check = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) +1):
        if check[i] == True:
            j = 2
            while i * j <= n:
                check[i * j] = False
                j += 1
    for i in range(2, n + 1):
        if check[i]:
            prime.append(i)

check_prime()
if n == 1:
    print(0)
    exit()

for x in range(len(prime)):
    cnt += prime[x]
    if cnt < n:
        continue
    elif cnt > n:
        while cnt > n:
            y += 1
            cnt -= prime[y]
        if cnt == n:
            ans += 1
    else:
        ans += 1

print(ans)