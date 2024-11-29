import sys
input = sys.stdin.readline

t = int(input())

def ispseudo(arr, left, right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def ispalindrome(arr):
    left, right = 0, len(arr)-1
    
    if arr == arr[::-1]:
        return 0
    else:
        while left < right:
            if arr[left] != arr[right]:
                check_left = ispseudo(arr, left + 1, right)
                check_right = ispseudo(arr, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

for _ in range(t):
    arr = input().strip()
    print(ispalindrome(arr))