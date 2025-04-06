import sys
input = sys.stdin.readline

t = int(input())
is_prime = [True] * 1299710
is_prime[0], is_prime[1] = False, False
for i in range(2, int(1299710 ** 0.5) + 2):
    if is_prime[i]:
        j = 2
        while j * i < 1299710:
            is_prime[j * i] = False
            j += 1

for _ in range(t):
    k = int(input())
    if is_prime[k]:
        print(0)
        continue

    i, j = 1, 1
    while not is_prime[k + i]:
        i += 1
    while not is_prime[k - j]:
        j += 1
    print(i + j)
