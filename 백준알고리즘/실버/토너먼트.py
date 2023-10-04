from math import log2
import sys
input = sys.stdin.readline

N, jimin, hansoo = map(int, input().split())

if (N // 2 <= jimin and N // 2 > hansoo) or (N // 2 > jimin and N // 2 <= hansoo):
  print(int(log2(N)))
  exit()
  
while (N < jimin and N < hansoo) or (N > jimin and N > hansoo):
  N //= 2

print(int(log2(N)))