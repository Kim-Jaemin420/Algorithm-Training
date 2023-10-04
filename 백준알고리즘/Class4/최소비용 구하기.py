from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = int(input()), int(input())
graph = defaultdict(list)
INF = 1e9
dp = [INF] * (N + 1)

for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u].append([w, v])

start, end = map(int, input().split())

def dijkstra(start):
  heap = []
  heapq.heappush(heap, [0, start])
  
  while heap:
    currentWeight, currentNode = heapq.heappop(heap)
    
    if currentWeight < dp[currentNode]:
      dp[currentNode] = currentWeight
    else:
      continue
    
    for nextWeight, nextNode in graph[currentNode]:
      if dp[nextNode] > nextWeight + currentWeight:
        heapq.heappush(heap, [nextWeight + currentWeight, nextNode])
    

dijkstra(start)
print(dp[end])