import sys
input = sys.stdin.readline

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]

def countPaper(x, y, n):
  value = papers[x][y]
  
  for i in range(x, x + n):
    for j in range(y, y + n):
      if papers[i][j] != value:
        n //= 3
        countPaper(x, y, n)
        countPaper(x + 2 * n, y, n)
        countPaper(x, y + 2 * n, n)
        countPaper(x + n, y, n)
        countPaper(x + n, y + 2 * n, n)
        countPaper(x, y + n, n)
        countPaper(x + n, y + n, n)
        countPaper(x + 2 * n, y + n, n)
        countPaper(x + 2 * n, y + 2 * n, n)
        return
  answer[value] += 1

countPaper(0, 0, N)
print(answer[-1])
print(answer[0])
print(answer[1])
