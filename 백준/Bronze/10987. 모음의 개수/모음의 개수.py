import sys
input = sys.stdin.readline

vowels = ["a", "e", "i", "o", "u"]
ans = 0
arr = list(input().strip())

for x in arr:
    if x in vowels:
        ans += 1
print(ans)