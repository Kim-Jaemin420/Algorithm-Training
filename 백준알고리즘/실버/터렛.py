import math
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
  radiusSum = r1 + r2
  radiusDifference = abs(r1 - r2)
  
  if radiusDifference < distance < radiusSum:
    print(2)
  elif distance == radiusDifference or distance == radiusSum:
    print(1)
  elif distance == 0 and r1 == r2:
    print(-1)
  else:
    print(0)