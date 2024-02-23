N,B=map(int,input().split())

alpha=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result=''

while N>0:
    result+=alpha[N%B]
    N//=B

print(result[::-1])