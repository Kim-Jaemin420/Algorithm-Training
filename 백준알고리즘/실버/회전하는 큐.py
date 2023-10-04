from collections import deque
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
pickUpLocations = list(map(int, input().split()))
queue = [i + 1 for i in range(N)]
count = 0

while pickUpLocations:
  pickUpLocation = pickUpLocations.pop(0)
  
  pickUpIndex = queue.index(pickUpLocation)
  
  if pickUpIndex == 0:
    queue.pop(0)
    continue
  elif pickUpIndex > len(queue) // 2:
    count += len(queue) - pickUpIndex
    queue = queue[pickUpIndex:] + queue[0:pickUpIndex]
    queue.pop(0)
  elif pickUpIndex <= len(queue) // 2:
    count += pickUpIndex
    queue = queue[pickUpIndex:] + queue[0:pickUpIndex]
    queue.pop(0)

print(count)