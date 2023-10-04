from itertools import combinations
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chickenShops = []
houses = []
distance = 1e10

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      houses.append((i, j))
    if graph[i][j] == 2:
      chickenShops.append((i, j))
      
cases = list(combinations(chickenShops, M))

def calculateChickenDistance(chickenShops):
  distance = [1e10] * len(houses)
  
  for i in range(len(houses)):
    for chickenShop in chickenShops:
      x, y = chickenShop
      distance[i] = min(distance[i], abs(houses[i][0] - x) + abs(houses[i][1] - y))

  return sum(distance)
      
for case in cases:
  distance = min(distance, calculateChickenDistance(case))

print(distance)