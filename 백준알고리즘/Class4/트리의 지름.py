from collections import defaultdict
import heapq
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

n = int(input())
graph = defaultdict(list)

for _ in range(n):
  parent, child, weight = map(int, input().split())
  graph[parent].append([-weight, child])

def dfs():
  heap = []
  heapq.heappush([0, 1])
  
  while heap:
    currentWeight, currentNode = heapq.heappop()
    
    for weight, node in graph[currentNode]:
      pass
    

dfs()