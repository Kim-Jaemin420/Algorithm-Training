import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10 ** 5
distance = [0] * (MAX + 1)

# dp로 풀고 싶었으나 풀이가 복잡해지고 답도 계속 틀림ㅠ
# def hideAndSeek():
  # dp = { N + i: i for i in range(-1, K - N + 3) }

#   if N >= K:
#     return N - K
#   else:
#     dp[N - 1], dp[N * 2] = 1, 1
    
#     for i in range(N, N * 2):
#       if i % 2 == 0 and i // 2 >= N - 1:
#         dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1, dp[N * 2] + N * 2 - i, dp[i // 2] + 1)
#       else:
#         dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1, dp[N * 2] + N * 2 - i)
#       dp[i - 1] = min(dp[i - 1], dp[i] + 1)
#       dp[i + 1] = min(dp[i + 1], dp[i] + 1)


#     for i in range(N * 2 + 1, K + 2):
#       if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1, dp[i + 1] + 1, dp[i - 1] + 1)
#         dp[i - 1] = min(dp[i - 1], dp[i] + 1)
#         dp[i + 1] = min(dp[i + 1], dp[i] + 1)
#       else:
#         dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1)
    
#     return dp[K]
    
  
# print(hideAndSeek())
def bfs():
  q = deque()
  q.append(N)
  
  while q:
    number = q.popleft()
    
    if number == K:
      print(distance[number])
      break
    
    for jump_number in (number - 1, number + 1, number * 2):
      if 0 <= jump_number <= MAX and distance[jump_number] == 0:
        distance[jump_number] = distance[number] + 1
        q.append(jump_number)
bfs()    
