x = input()
y = input()
A = int(x)
B = int(y)
print(A*(B%10))
print(A*((B//10)%10))
print(A*(B//100))
print(A*B)