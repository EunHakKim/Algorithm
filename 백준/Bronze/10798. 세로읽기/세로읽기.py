b=[]

for _ in range(5):
    a=list(input())
    b.append(a)

for i in range(max(len(b[0]),len(b[1]),len(b[2]),len(b[3]),len(b[4]))):
    for j in range(5):
        try:
            print(b[j][i], end="")
        except:
            pass