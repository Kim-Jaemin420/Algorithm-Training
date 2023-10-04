import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)
res = 0

while len(cards) > 1:
  a, b = heapq.heappop(cards), heapq.heappop(cards)
  res += a + b
  heapq.heappush(cards, a + b)

print(res)