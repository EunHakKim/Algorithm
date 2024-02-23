N=int(input())

binary0=[0,0,1,1]
binary1=[0,1,0,1]

for i in range(4,N+1):
    binary0.append(binary0[i-1]+binary1[i-1])
    binary1.append(binary0[i-1])

print(binary0[N]+binary1[N])