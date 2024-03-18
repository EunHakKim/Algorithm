a,b,c,d,e,f=map(int,input().split())

x=int((b*f-e*c)/(b*d-e*a))
y=int((a*f-d*c)/(a*e-b*d))

print(x,y)