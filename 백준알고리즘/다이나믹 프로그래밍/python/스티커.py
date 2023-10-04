import sys
input = sys.stdin.readline

T = int(input())

# 시간초과 풀이..
# for _ in range(T):
#   n = int(input())
#   stickers = [(n, i, j) for i in range(2) for j, n in enumerate(map(int, input().split()))]
#   stickers.sort(key=lambda x: -x[0])
  
#   result = []
  
#   while stickers:
#     sticker = stickers.pop(0)
#     number, i, j = sticker
#     result.append(sticker)
    
#     for sticker in stickers[:]:
#       if (sticker[1] == i - 1 and sticker[2] == j) or (sticker[1] == i and sticker[2] == j - 1) or (sticker[1] == i and sticker[2] == j + 1) or (sticker[1] == i + 1 and sticker[2] == j):
#         stickers.remove(sticker)
    
#   answer = 0
#   for res in result:
#     answer += res[0]
#   print(answer)

for _ in range(T):
  n = int(input())
  stickers = [list(map(int, input().split())) for _ in range(2)]
  
  for j in range(1, n):
    if j == 1:
      stickers[0][j] += stickers[1][0]
      stickers[1][j] += stickers[0][0]
    else:
      stickers[0][j] += max(stickers[1][j - 1], stickers[1][j - 2])
      stickers[1][j] += max(stickers[0][j - 1], stickers[0][j - 2])
  
  print(max(sum(stickers, [])))
  