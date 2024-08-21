import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int,input().split()))
result = 0

for i in range(1, w-1):
    result += min(max(height[:i+1]), max(height[i:]))
    result -= height[i]

print(result)