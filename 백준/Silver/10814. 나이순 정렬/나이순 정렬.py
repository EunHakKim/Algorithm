n=int(input())
result=[]

for i in range(n):
    [age, name]=list(input().split())
    result.append([int(age),name])

result.sort(key=lambda x:x[0])

for i in range(n):
    print(result[i][0],result[i][1])
