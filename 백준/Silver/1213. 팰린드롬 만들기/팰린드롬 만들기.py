import sys
from collections import Counter
input=sys.stdin.readline

name=sorted(list(input().strip()))
cnt=Counter(name)
a=0
mid=""
result=""

for k,v in cnt.items():
    if v%2==1:
        a+=1
        mid=k
        if a>=2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in cnt.items():
    result += (k * (v // 2))
result=result+mid+result[::-1]
print(result)