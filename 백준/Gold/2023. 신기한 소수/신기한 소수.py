import sys
import math
input = sys.stdin.readline

n = int(input())
f_prime = [2,3,5,7]
prime = [1,3,7,9]

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def back(depth, ans):
    if depth==n:
        print(ans)
        return

    for i in range(4):
        if depth==0:
            back(depth+1, ans+str(f_prime[i]))
        else:
            num = int(ans + str(prime[i]))
            if isPrime(num):
                back(depth+1, ans+str(prime[i]))

back(0, "")