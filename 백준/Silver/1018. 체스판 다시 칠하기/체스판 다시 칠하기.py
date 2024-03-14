n,m=map(int,input().split())

c=[]

a=["BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB"
]

result=64

for i in range(n):
    wb=input()
    c.append(wb)

for i in range(n-7):
    for j in range(m-7):
        count=0
        for k in range(8):
            for h in range(8):
                if c[i+k][j+h]!=a[k][h]:
                    count+=1
        if count>32:
            count=64-count
        if count<result:
            result=count

print(result)
