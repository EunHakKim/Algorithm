n=int(input())

for i in range(n):
    words=list(input().split())
    for x in words:
        print(x[::-1],end=" ")
    print()