A,B=map(int,input().split())
m=int(input())
Anum=list(map(int,input().split()))
Bnum=[]
num=0

for i in range(len(Anum)):
    num+=Anum[(-1)*(i+1)]*(A**i)

while num>0:
    Bnum.append(num%B)
    num//=B

for i in range(1,len(Bnum)+1):
    print(Bnum[(-1)*i],end=" ")