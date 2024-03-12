L,C=map(int,input().split())
arr=list(map(str,input().split()))
arr=sorted(arr)
result=[]

def backtracking():
    if len(result)==L:
        vowels=0
        consonants=0
        for y in result:
            if y in 'aeiou':
                vowels+=1
            else:
                consonants+=1
        if vowels>0 and consonants>1:
            for y in result:
                print(y, end="")
            print()
        return


    for x in arr:
        if len(result)==0 or x>result[-1]:
            result.append(x)
            backtracking()
            result.pop()

backtracking()