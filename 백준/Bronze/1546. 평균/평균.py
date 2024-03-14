n=int(input())

num=list(map(int,input().split()))

a=[num[i]/max(num)*100 for i in range(n)]

print(sum(a)/len(a))