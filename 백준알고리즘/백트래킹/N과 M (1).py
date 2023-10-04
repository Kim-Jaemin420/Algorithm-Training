import sys
import itertools
input = sys.stdin.readline

# N, M = map(int, input().split())
# nums = [i for i in range(1, N + 1)]
# result = list(itertools.permutations(nums, M))

# for i in result:
#   print(*i)


N, M = map(int, input().split())
visited = [False] * N
print_list = []

def backTracking(depth):
  if depth == M:
    print(*print_list)
    return
  
  for i in range(N):
    if not visited[i]:
      visited[i] = True
      print_list.append(i + 1)
      backTracking(depth + 1)
      visited[i] = False
      print_list.pop()

backTracking(0)
