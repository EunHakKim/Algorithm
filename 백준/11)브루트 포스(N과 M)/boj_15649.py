N, M = map(int, input().split())
result=[str(x) for x in range(1,N+1)]
new_result=[]

while(M>1):
    for i in range(len(result)):
        for j in range(1,N+1):
            if str(j) not in result[i]:
                new_result.append(result[i]+str(j))
    result=new_result
    new_result=[]
    M-=1

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=" ")
    print()
