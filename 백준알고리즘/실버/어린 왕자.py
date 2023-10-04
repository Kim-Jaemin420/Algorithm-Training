import math
import sys
input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  count = 0
  
  for _ in range(n):
    cx, cy, r = map(int, input().split())
    
    startDistance = math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
    endDistance = math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2)
    
    if startDistance <= r:
      count += 1