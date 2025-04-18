import sys

input = sys.stdin.readline

arr = []

def check(n):
    expression, ans = "1", "1"
    for i in range(n - 1):
        if arr[i] == 0:
            expression += '+' + str(i + 2)
            ans += '+' + str(i + 2)
        elif arr[i] == 1:
            expression += '-' + str(i + 2)
            ans += '-' + str(i + 2)
        else:
            expression += ' ' + str(i + 2)
            ans += ' ' + str(i + 2)

    temp = ""
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            j = i - 1
            while j >= 0 and expression[j] == ' ':
                j -= 1
            start = j
            while start >= 0 and expression[start].isdigit():
                start -= 1
            start += 1
            left = expression[:start]
            num = ""
            k = start
            while k < len(expression) and (expression[k].isdigit() or expression[k] == ' '):
                if expression[k] != ' ':
                    num += expression[k]
                k += 1
            right = expression[k:]
            expression = left + num + right
            i = start + len(num) - 1
        else:
            i += 1

    total = 0
    num = ""
    op = '+'
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            if num:
                if op == '+':
                    total += int(num)
                else:
                    total -= int(num)
                num = ""
            op = ch
    if num:
        if op == '+':
            total += int(num)
        else:
            total -= int(num)

    if total == 0:
        print(ans)


def back(n):
    if len(arr) == n - 1:
        check(n)
        return
    for k in [2, 0, 1]:
        arr.append(k)
        back(n)
        arr.pop()


t = int(input())
for tc in range(t):
    n = int(input())
    back(n)
    print()