n = int(input())
ans = 99

if n < 100:
    print(n)
    exit()

for i in range(100, n + 1):
    arr = str(i)
    if int(arr[2]) - int(arr[1]) == int(arr[1]) - int(arr[0]):
        ans += 1
print(ans)