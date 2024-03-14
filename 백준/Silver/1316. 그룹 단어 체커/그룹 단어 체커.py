n=int(input())

num=n

for i in range(n):
    a=input()
    for j in range(len(a)-1):
        if a[j]==a[j+1]:
            pass
        elif a[j] in a[j+1:]:
            num-=1
            break

print(num)