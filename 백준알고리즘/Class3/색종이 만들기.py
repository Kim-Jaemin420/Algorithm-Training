import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

def makeConfetti(x, y, n):
  value = graph[x][y]
  
  for i in range(x, x + n):
    for j in range(y, y + n):
      if graph[i][j] != value:
        n //= 2
        makeConfetti(x, y, n)
        makeConfetti(x, y + n, n)
        makeConfetti(x + n, y, n)
        makeConfetti(x + n, y + n, n)
        return
  answer[value] += 1
        

makeConfetti(0, 0, N)

print(answer[0])
print(answer[1])