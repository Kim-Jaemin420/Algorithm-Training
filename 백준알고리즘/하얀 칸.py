import sys
input = sys.stdin.readline

BOARD_SIZE = 8
WHITE = True
BLACK = False
CHESS_PIECE = 'F'

chessBoard = []
answer = 0

for i in range(BOARD_SIZE):
  if i % 2 == 0:
    chessBoard.append([WHITE if j % 2 == 0 else BLACK for j in range(BOARD_SIZE)])
  else:
    chessBoard.append([BLACK if j % 2 == 0 else WHITE for j in range(BOARD_SIZE)])

for i in range(BOARD_SIZE):
  chessBoardState = list(input().rstrip())
  
  for j in range(BOARD_SIZE):
    if chessBoard[i][j] and chessBoardState[j] == CHESS_PIECE:
      answer += 1

print(answer)