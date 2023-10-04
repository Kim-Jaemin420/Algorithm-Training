import sys
input = sys.stdin.readline


L = int(input())
S = list(map(int, input().split()))
s = int(input())

S.append(0)
S.sort()

answer = 0
for i in range(len(S)-1) :
    if S[i] == s or S[i+1] == s:
        answer = 0
        break
    elif S[i] < s and s < S[i+1]:
        answer = (s - S[i]) * (S[i+1] - s) - 1
        break

print(answer)
answer = 0

S.sort()

if s in S:
  print(0)
  # exit(0)
  
maximum, minimum = 0, 0

for i in range(L):
  if S[i] > s:
    maximum = S[i] - 1
    if S[i - 1] < s:
      minimum = S[i - 1] + 1
    break

answer += maximum - s + 1 + 1 + (maximum - s + 1) * (s - minimum)
print(answer)