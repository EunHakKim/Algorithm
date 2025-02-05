import sys
input = sys.stdin.readline

n = int(input())
ports = list(map(int, input().split()))

def binary_search(result, port):
    st, en = 0, len(result) - 1
    while st < en:
        mid = (st + en) // 2
        if result[mid] < port:
            st = mid + 1
        else:
            en = mid
    return st

result = [ports[0]]

for i in range(1, n):
    if result[-1] < ports[i]:
        result.append(ports[i])
    else:
        result[binary_search(result, ports[i])] = ports[i]

print(len(result))
