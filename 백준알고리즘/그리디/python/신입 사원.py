import sys
input = sys.stdin.readline

def solution():
  N = int(input())
  recruits = []
  res = 1

  for _ in range(N):
    recruits.append(tuple(map(int, input().split())))
  
  recruits.sort(key=lambda x: (x[0]))
  
  p = recruits[0]
  for i in range(1, N):
    if recruits[i][1] < p[1]:
      p = recruits[i]
      res += 1
  
  return res


for _ in range(int(input())):
  print(solution())