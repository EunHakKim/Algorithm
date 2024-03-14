n=int(input())

if n==1:
    print("1")
elif n==2:
    print("2")
else:
    sum=(n-2)//6+1
    result=0
    i=0
    while result<sum:
        i+=1
        result+=i
    print(i+1)

