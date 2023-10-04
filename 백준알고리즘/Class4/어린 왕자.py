import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
  x1, y1, x2, y2 = map(int, input().split())
  