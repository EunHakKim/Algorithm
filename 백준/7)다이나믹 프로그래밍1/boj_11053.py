N=int(input())
A=list(map(int,input().split()))

longA=[]

for i in range(N):
    if i==0:
        longA.append(A[i])
    elif A[i]>longA[-1]:
        longA.append(A[i])
    elif A[i]==longA[-1]:
        pass
    else:
        for j in range(len(longA)):
            if A[i]<longA[j]:
                longA[j]=A[i]
                break

print(len(longA))