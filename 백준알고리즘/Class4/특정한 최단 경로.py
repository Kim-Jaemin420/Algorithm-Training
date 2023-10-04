from collections import defaultdict, deque
import heapq
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')
N, E = map(int, input().split())
graph = defaultdict(list)
INF = 1e10

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append([c, b])
  graph[b].append([c, a])

v1, v2 = sorted(map(int, input().split()))

def dijkstra(start, end):
  distance = [INF] * (N + 1)
  distance[start] = 0  
  heap = []
  heapq.heappush(heap, [0, start])
  
  while heap:
    currentDistance, currentNode = heapq.heappop(heap)
    
    if currentNode == end:
      continue
    
    for connectedDistance, connectedNode in graph[currentNode]:
      newDistance = connectedDistance + currentDistance
      if distance[connectedNode] > newDistance:
        distance[connectedNode] = newDistance
        heapq.heappush(heap, [newDistance, connectedNode])
  
  return distance[end]

specificDistance = dijkstra(v1, v2)
v1toEnd = dijkstra(1, v1) + specificDistance + dijkstra(v2, N)
v2toEnd = dijkstra(1, v2) + specificDistance + dijkstra(v1, N)

if v1toEnd == INF and v2toEnd == INF:
  print(-1)
else:
  print(min(v1toEnd, v2toEnd))