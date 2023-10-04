import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
brokenButtons = list(map(int, input().split()))
INIT_CHANNEL = 100
answer = abs(INIT_CHANNEL - N)

for nearChannel in range(1000001):
  
  for i in range(len(str(nearChannel))):
    if int(str(nearChannel)[i]) in brokenButtons:
      break
    
    if i == len(str(nearChannel)) - 1:
      answer = min(answer, len(str(nearChannel)) + abs(nearChannel - N))
  
print(answer)  