a,b,c=map(int, input().split())

if max(a,b,c)<a+b+c-max(a,b,c):
    print(a+b+c)
else:
    print(2*(a+b+c-max(a,b,c))-1)