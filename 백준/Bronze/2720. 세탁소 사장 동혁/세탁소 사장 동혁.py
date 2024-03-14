n=int(input())

for i in range(n):
    money=int(input())
    rest=[]
    rest.append(money//25)
    money%=25
    rest.append(money//10)
    money%=10
    rest.append(money//5)
    money%=5
    rest.append(money//1)
    money%=1
    print(rest[0],rest[1],rest[2],rest[3])
