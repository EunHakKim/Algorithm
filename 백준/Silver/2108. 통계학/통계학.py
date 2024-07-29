import sys
input = sys.stdin.readline

n = int(input())
nums = []
frequency = [0]*8001
sum = 0
for _ in range(n):
    i = int(input())
    sum += i
    frequency[i+4000]+=1
    nums.append(i)

nums.sort()
m = max(frequency)
ans = frequency.index(m)
frequency[ans] = 0
if m in frequency:
    ans = frequency.index(m)

print(round(sum/n))
print(nums[n//2])
print(ans - 4000)
print(nums[-1]-nums[0])