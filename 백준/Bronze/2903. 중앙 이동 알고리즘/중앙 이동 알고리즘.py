n=int(input())

result=2

def a(i):
    return i*2-1

for i in range(n):
    result=a(result)

print(result**2)