while True:
    n=int(input())
    if n==-1:
        break

    num=[]

    for i in range(1,n):
        if n%i==0:
            num.append(i)

    if sum(num)==n:
        print(f"{n} =",end=" ")
        for i in range(len(num)-1):
            print(f"{num[i]} +",end=" ")
        print(num[-1])
    else:
        print(f"{n} is NOT perfect.")    
