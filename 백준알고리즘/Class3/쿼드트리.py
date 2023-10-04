import sys
input = sys.stdin.readline

N = int(input())
videos = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def quadTree(x, y, n):
  value = videos[x][y]
  
  for i in range(x, x + n):
    for j in range(y, y + n):
      if videos[i][j] != value:
        print('(', end='')
        n //= 2
        quadTree(x, y, n)
        quadTree(x, y + n, n)
        quadTree(x + n, y, n)
        quadTree(x + n, y + n, n)
        print(')', end='')
        return
      
  if value == 1:
    print('1', end='')
    return
  else:
    print('0', end='')
    return

quadTree(0, 0, N)