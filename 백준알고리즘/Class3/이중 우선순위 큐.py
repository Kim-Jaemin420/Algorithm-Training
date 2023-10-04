import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  k = int(input())
  minHeap = []
  maxHeap = []
  done = [False] * k
  
  for index in range(k):
    command, number = input().split()
    number = int(number)
    
    if command == 'I':
      heapq.heappush(minHeap, (number, index))
      heapq.heappush(maxHeap, (-number, index))

    if command == 'D':
      if number == -1:
        while minHeap:
          if done[minHeap[0][1]]:
            heapq.heappop(minHeap)
          else:
            break
        if minHeap:
          minIndex = minHeap[0][1]
          done[minIndex] = True
      if number == 1:
        while maxHeap:
          if done[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
          else:
            break
        if maxHeap:
          maxIndex = maxHeap[0][1]
          done[maxIndex] = True
  
  while maxHeap:
          if done[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
          else:
            break
  while minHeap:
          if done[minHeap[0][1]]:
            heapq.heappop(minHeap)
          else:
            break
  
  if minHeap:
    print(-maxHeap[0][0], minHeap[0][0])
  else:
    print('EMPTY')
        

