from collections import deque
import sys
input = sys.stdin.readline

# sys.stdin = open('input.txt', 'r')
N, K = map(int, input().split())
bottleToBuy = 0
bottles = deque()
totalBottles = N
count = 1

while totalBottles > 0:
  if totalBottles % 2 != 0:
    bottles.append([count, ])
  totalBottles //= 2
  
    