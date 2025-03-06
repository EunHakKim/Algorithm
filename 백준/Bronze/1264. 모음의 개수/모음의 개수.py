import sys
input = sys.stdin.readline

mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    arr = list(input().strip())
    ans = 0
    if arr[0] == '#':
        exit()
    for x in arr:
        if x in mo:
            ans += 1
    print(ans)