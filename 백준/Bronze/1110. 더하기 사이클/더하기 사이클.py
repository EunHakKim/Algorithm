n = input().rstrip()
ans = 0
first_num = n

while True:
    ans += 1
    if len(n) == 1:
        n += n
    else:
        temp = str(int(n[0]) + int(n[-1]))
        n = n[-1] + temp[-1]

    if int(n) == int(first_num):
        break

print(ans)