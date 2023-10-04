import sys
input = sys.stdin.readline

N = int(input())

answer = 0
result = 1

for i in range(1, N + 1):
  result *= i


for i in str(result)[::-1]:
  if i != '0':
    print(answer)
    break
  else:
    answer += 1