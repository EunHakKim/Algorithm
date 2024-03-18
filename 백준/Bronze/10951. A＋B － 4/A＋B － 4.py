import sys

while True :
    try:
        x,y = sys.stdin.readline().split()
        if(int(x)==0 and int(y)==0):
            break
        print(int(x)+int(y))
    except:
        break