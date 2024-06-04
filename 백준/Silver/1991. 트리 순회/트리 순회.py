from collections import deque

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())

leftChild = [-1]*26
rightChild = [-1]*26
preorder=""
inorder=""
postorder=""


for _ in range(N):
    str = input().split()
    if(str[1]!='.'):
        leftChild[alpha.index(str[0])]=alpha.index(str[1])
    if(str[2]!='.'):
        rightChild[alpha.index(str[0])]=alpha.index(str[2])

def dfs(index):
    global preorder
    global inorder
    global postorder
    preorder+=alpha[index]
    if leftChild[index]!=-1:
        dfs(leftChild[index])
    inorder+=alpha[index]
    if rightChild[index]!=-1:
        dfs(rightChild[index])
    postorder+=alpha[index]

dfs(0)
print(preorder)
print(inorder)
print(postorder)