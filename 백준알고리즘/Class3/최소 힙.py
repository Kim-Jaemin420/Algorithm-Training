import sys
import heapq
input = sys.stdin.readline

N = int(input())
minHeap = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    print(heapq.heappop(minHeap) if minHeap else 0)
  else:
    heapq.heappush(minHeap, x)
