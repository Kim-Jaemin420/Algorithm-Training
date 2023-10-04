import sys
import heapq
input = sys.stdin.readline

N = int(input())
maxHeap = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    print(-heapq.heappop(maxHeap) if maxHeap else 0)
  else:
    heapq.heappush(maxHeap, -x)