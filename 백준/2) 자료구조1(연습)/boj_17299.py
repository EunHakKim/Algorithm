import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b=[0]*1000001

result=[-1]*n
stack=[0]

for i in range(n):
    b[a[i]]+=1

for i in range(1, n):
    while stack and b[a[stack[-1]]] < b[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)


print(*result)