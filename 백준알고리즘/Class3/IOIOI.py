import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
answer = 0
count = 0
P1 = 'IOI'

i = 0
while i < M - 2:
  if S[i:i + 3] == P1:
    i += 2
    count += 1
    if count == N:
      answer += 1
      count -= 1
  else:
    i += 1
    count = 0
    
print(answer)
