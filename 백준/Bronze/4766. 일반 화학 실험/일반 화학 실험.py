import sys
import math
input = sys.stdin.readline

tem1 = float(input())
while True:
    tem2 = float(input())
    if tem2==999:
        exit()
    print(f"{tem2-tem1:.2f}")
    tem1=tem2