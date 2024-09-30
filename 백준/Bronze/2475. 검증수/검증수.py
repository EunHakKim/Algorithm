import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
sum = 0
for x in arr:
    sum = (sum + x ** 2) % 10
    
print(sum)