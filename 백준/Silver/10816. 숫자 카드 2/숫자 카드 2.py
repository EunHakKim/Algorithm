import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
target_list = list(map(int, input().split()))

card_dic = {}
for card in cards:
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

def search(st, en, target):
    if st > en:
        print(0, end = " ")
        return
    mid = (st + en) // 2
    if cards[mid] > target:
        search(st, mid - 1, target)
    elif cards[mid] < target:
        search(mid + 1, en, target)
    else:
        print(card_dic[target], end = " ")
        return

for target in target_list:
    search(0, n-1, target)