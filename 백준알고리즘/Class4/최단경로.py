import heapq
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)

graph = [[] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

answer = [INF] * (V + 1)


def dijkstra(start):
  answer[start] = 0
  heap = []
  heapq.heappush(heap, (0, start))
  while heap:
    w, node = heapq.heappop(heap)
    if answer[node] < w:
      continue

    for next_weight, next_node  in graph[node]:
      if answer[next_node] > next_weight + w:
        answer[next_node] = next_weight + w
        heapq.heappush(heap, (next_weight + w, next_node))
  
dijkstra(K)


for i in answer[1:]:
  if i == INF:
    print("INF")
  else:
    print(i)