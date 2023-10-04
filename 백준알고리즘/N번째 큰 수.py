import heapq
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N = int(input())
heap = []

for _ in range(N):
  numbers = list(map(int, input().split()))
  
  if not heap:
    for number in numbers:
      heapq.heappush(heap, number)
  
  else:
    for number in numbers:
      if heap[0] < number:
        heapq.heappop(heap)
        heapq.heappush(heap, number)

print(heap[0])