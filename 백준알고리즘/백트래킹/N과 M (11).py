import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * N
visited_list = {}
sequence_list = []

def backTracking(depth):
  if depth == M:
    temp = ' '.join(map(str, sequence_list))
    if temp not in visited_list:
      visited_list[temp] = 1
      print(temp)
  
    return
  
  for i in range(N):
    sequence_list.append(numbers[i])
    backTracking(depth + 1)
    sequence_list.pop()

backTracking(0)