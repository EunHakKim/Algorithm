A, B = input().split()
x=int(A)
y=int(B)
z=int(input())

if y+z<60 :
    print(x, y+z)
elif y+z>=60 and x+((y+z)//60)<24 :
    print(x+((y+z)//60),(y+z)%60)
elif y+z>=60 and x+((y+z)//60)>=24 :
    print(x+((y+z)//60)-24,(y+z)%60)