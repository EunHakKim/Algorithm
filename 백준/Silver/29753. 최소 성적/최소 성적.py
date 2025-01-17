import sys
input = sys.stdin.readline

abcdf = {'A+': 4.5, 'A0': 4.0, 
         'B+': 3.5, 'B0': 3.0, 
         'C+': 2.5, 'C0': 2.0, 
         'D+': 1.5, 'D0': 1.0, 
         'F': 0.0, }
n, x = map(float, input().split())
n = int(n)
x = int(round(x * 100))
grade = 0.0
count = []

for i in range(n - 1):
    arr = list(input().strip().split())
    count.append(int(arr[0]))
    grade += int(arr[0]) * abcdf[arr[1]]

count.append(int(input()))

for key, value in reversed(abcdf.items()):
    result = int(((grade + count[-1] * value) * 100) / sum(count))
    if result > x:
        print(key)
        exit()

print("impossible")