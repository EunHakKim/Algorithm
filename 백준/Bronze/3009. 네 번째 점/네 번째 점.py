a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

if a==c and a!=e:
    print(e,end=" ")
elif a==e and a!=c:
    print(c,end=" ")
elif c==e and c!=a:
    print(a,end=" ")

if b==d and b!=f:
    print(f,end=" ")
elif b==f and b!=d:
    print(d,end=" ")
elif d==f and d!=b:
    print(b,end=" ")