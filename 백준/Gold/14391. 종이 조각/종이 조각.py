N, M = map(int, input().split())
paper = [list(map(int, input().rstrip())) for _ in range(N)]

result = 0

for case in range(1 << (N*M)):

    total = 0

    for i in range(N):
        rowsum = 0
        for j in range(M):
            idx = (i*M) + j
            if case & (1 << idx):
                rowsum = rowsum*10 + paper[i][j]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    for j in range(M):
        colsum = 0
        for i in range(N):
            idx = (i*M) + j
            if not (case & (1 << idx)):
                colsum = colsum*10 + paper[i][j]
            else:
                total += colsum
                colsum = 0
        total += colsum

    result = max(result, total)

print(result)