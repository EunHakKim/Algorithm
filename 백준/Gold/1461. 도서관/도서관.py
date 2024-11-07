import sys
input = sys.stdin.readline

n, m = map(int,input().split())
books = list(map(int,input().split()))
books_p = []
books_m = []

for book in books:
    if book > 0:
        books_p.append(book)
    else:
        books_m.append(-book)

books_m.sort(reverse=True)
books_p.sort(reverse=True)

def sum(book_list):
    index = 0
    ans = 0
    while index < len(book_list):
        ans += 2 * book_list[index]
        index += m
    return ans

if len(books_p) == 0 and len(books_m) == 0:
    print(0)
elif len(books_p) == 0:
    print(sum(books_m) - max(books_m))
elif len(books_m) == 0:
    print(sum(books_p) - max(books_p))
else:
    print(sum(books_m) + sum(books_p) - max(max(books_m), max(books_p)))
