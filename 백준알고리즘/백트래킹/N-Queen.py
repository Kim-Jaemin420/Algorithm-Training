import sys
input = sys.stdin.readline

N = int(input())
chess_board = [[True for _ in range(N)] for _ in range(N)]
print(chess_board)
visited_list = []

def dfs():
  pass

def solution():
  for i in range(N):
    for j in range(N):
      chess_board[i][j] = True
      
    
    dfs(0, i)
    