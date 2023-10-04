from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
friendsGraph = defaultdict(list)
answer = [0] * (N + 1)
# 처음엔 풀었는데 두번째는 왜 버벅거리냐
for _ in range(M):
  A, B = map(int, input().split())
  friendsGraph[A].append(B)
  friendsGraph[B].append(A)

for i in range(1, N + 1):
  visited = [False] * (N + 1)
  visited[i] = True
  
  count = [0] * (N + 1)
  queue = deque([(j, i) for j in friendsGraph[i]])
  while queue:
    currentValue = queue.popleft()
    
    if visited[currentValue[0]]:
      continue
    
    visited[currentValue[0]] = True
    queue.extend([(j, currentValue[0]) for j in friendsGraph[currentValue[0]]])
    count[currentValue[0]] = count[currentValue[1]] + 1
  
  answer[i] = sum(count)

print(answer.index(min(answer[1:])))
  