k=int(input())
relation=list(map(str,input().split()))
arr_big=[]
arr_small=[]

def backtracking_big(depth):
    if len(arr_big)==k+1:
        for x in arr_big:
            print(x, end="")
        print()
        backtracking_small(0)
        exit()
    
    for i in range(9,-1,-1):
        if len(arr_big)==0:
            arr_big.append(i)
            backtracking_big(depth)
            arr_big.pop()
        elif relation[depth]=='>' and i not in arr_big:
            if arr_big[-1]>i:
                arr_big.append(i)
                backtracking_big(depth+1)
                arr_big.pop()
        elif relation[depth]=='<' and i not in arr_big:
            if arr_big[-1]<i:
                arr_big.append(i)
                backtracking_big(depth+1)
                arr_big.pop()

def backtracking_small(depth):
    if len(arr_small)==k+1:
        for x in arr_small:
            print(x, end="")
        print()
        exit()
    
    for i in range(10):
        if len(arr_small)==0:
            arr_small.append(i)
            backtracking_small(depth)
            arr_small.pop()
        elif relation[depth]=='>' and i not in arr_small:
            if arr_small[-1]>i:
                arr_small.append(i)
                backtracking_small(depth+1)
                arr_small.pop()
        elif relation[depth]=='<' and i not in arr_small:
            if arr_small[-1]<i:
                arr_small.append(i)
                backtracking_small(depth+1)
                arr_small.pop()

backtracking_big(0)