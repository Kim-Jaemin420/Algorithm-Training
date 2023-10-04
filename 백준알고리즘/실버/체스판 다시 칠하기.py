import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')
CHESS_SIZE = 8
INF = 1e9

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = INF
startBlackBoard = [
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ]

startWhiteBoard = [
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
  ]

def countRepaint(x, y):
  countBlack = 0
  countWhite = 0
   
  for i in range(x, x + CHESS_SIZE):
    for j in range(y, y + CHESS_SIZE):
     if board[i][j] != startBlackBoard[i - x][j - y]:
       countBlack += 1
     if board[i][j] != startWhiteBoard[i - x][j - y]:
        countWhite += 1
  return min(countBlack, countWhite)

for i in range(N - CHESS_SIZE + 1):
  for j in range(M - CHESS_SIZE + 1):
    answer = min(answer, countRepaint(i, j))

print(answer)