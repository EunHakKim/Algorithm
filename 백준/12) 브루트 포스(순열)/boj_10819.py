N=int(input())
A=list(map(int,input().split()))
arr=[]
result=[]

def backtracking():
    if len(arr)==N:
        sum=0
        for i in range(N-1):
            sum+=abs(arr[i]-arr[i+1])
        result.append(sum)
        return
    
    for x in A:
        if arr.count(x)<A.count(x):
            arr.append(x)
            backtracking()
            arr.pop()

backtracking()
print(max(result))