import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
bags.sort()


jewels.sort()

heap_jew = []
ans = 0

for bag in bags:
  while jewels and bag >= jewels[0][0]:
    heapq.heappush(heap_jew, -heapq.heappop(jewels)[1])
  
  if heap_jew:
    ans -= heapq.heappop(heap_jew)

  elif not jewels:
    break
print(ans)


