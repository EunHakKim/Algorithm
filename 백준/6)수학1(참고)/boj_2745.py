B,n=input().split()
B=list(B)
N=int(n)

alpha=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result=0
i=0

while B:
    result+=alpha.index(B.pop())*(N**i)
    i+=1

print(result)