N=int(input())
arr=list(map(int,input().split()))

check_arr=[x for x in range(N,0,-1)]
if arr==check_arr:
    print(-1)
    exit()

temp=[]
a=arr.pop()
b=arr.pop()

while(b>a):
    temp.append(a)
    a=b
    b=arr.pop()

temp.append(a)
mid_temp=[x for x in temp if x>b]
arr.append(min(mid_temp))
temp.remove(min(mid_temp))
temp.append(b)

while(len(temp)!=0):
    arr.append(min(temp))
    temp.remove(min(temp))

print(" ".join(map(str,arr)))