import sys
from math import factorial
input = sys.stdin.readline

T = int(input())

def ncr(n, r):
  return factorial(n) // (factorial(n-r) * factorial(r))

for _ in range(T):
  N, M = map(int, input().split())
  print(ncr(M, N))
