import sys
N=int(sys.stdin.readline())
N=str(N)
cnt=0

for i in range(len(N)-1):
    cnt += 9 * (i + 1) * 10 ** i

cnt += (int(N) - (10 ** (len(N) - 1)) + 1) * len(N)

print(cnt)