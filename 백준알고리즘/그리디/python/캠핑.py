import sys
input = sys.stdin.readline

L, P, V = map(int, input().split())
cnt = 1
ans = 0

while L != 0 and P != 0 and V != 0:
  if V % P < L:
    ans = (V // P) * L + (V % P)
  else:
    ans = (V // P) * L + L
  print('Case %d: %d' %(cnt, ans))
  cnt += 1
  L, P, V = map(int, input().split())