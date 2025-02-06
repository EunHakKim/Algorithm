import sys
from functools import cmp_to_key
input = sys.stdin.readline

def compare(a, b):
    if a + b > b + a: 
        return -1 
    elif a + b < b + a:
        return 1
    return 0 

n = int(input())
nums = list(input().strip().split())
nums.sort(key=cmp_to_key(compare))
ans = ''

for num in nums:
    ans += num

print(int(ans))