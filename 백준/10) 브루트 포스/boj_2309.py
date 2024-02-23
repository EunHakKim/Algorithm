arr=[]
for _ in range(9):
    arr.append(int(input()))

sum=sum(arr)

for i in range(8):
    if len(arr)==7:
        break
    for j in range(i+1,9):
        if sum-arr[i]-arr[j]==100:
            key1=arr[i]
            key2=arr[j]
            arr.remove(key1)
            arr.remove(key2)
            break

arr.sort()

for i in range(7):
    print(arr[i])