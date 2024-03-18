num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result=""

n,b=map(int,input().split())

while n!=0:
    result+=num[n%b]
    n//=b

print(result[::-1])