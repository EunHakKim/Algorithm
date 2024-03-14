n=int(input())
x,y=map(int,input().split())
maxx=x
minx=x
maxy=y
miny=y

if n==1:
    print("0")
else:
    for i in range(n-1):
        x,y=map(int,input().split())
        if x>=maxx:
            maxx=x
        if x<=minx:
            minx=x
        if y>=maxy:
            maxy=y
        if y<=miny:
            miny=y
    print((maxx-minx)*(maxy-miny))