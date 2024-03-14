A, B = input().split()
x=int(A)
y=int(B)
if y>=45 :
    print(x,y-45)
elif x!=0 and y<45 :
    print(x-1,60+y-45)
elif x==0 and y<45 :
    print("23",60+y-45)