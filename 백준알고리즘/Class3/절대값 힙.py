import sys
import heapq
input = sys.stdin.readline

N = int(input())
absoluteHeap = []

for _ in range(N):
  number = int(input())
  if number != 0:
    heapq.heappush(absoluteHeap, (abs(number), number))
  else:
    print(heapq.heappop(absoluteHeap)[1] if absoluteHeap else 0)