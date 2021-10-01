import sys
input = sys.stdin.readline

S = list(input())
N = len(S)
target = S[0]
i_list = []

for i in range(1, N):
  if S[i] != target:
    target = S[i]
    i_list.append(i)

if len(i_list) % 2:
  print((len(i_list) - 1 )// 2)
else:
  print(len(i_list) // 2)