A, B = map(int,input().split())
x=(A%10)*100+((A//10)%10)*10+A//100
y=(B%10)*100+((B//10)%10)*10+B//100
print(max(x,y))