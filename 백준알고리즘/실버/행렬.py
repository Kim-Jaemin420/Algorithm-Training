import sys
input = sys.stdin.readline

CONVERSION_SIZE = 3
N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]
# C = A[:]
answer = []


def conversion(x, y, C, count):
  count += 1
  print(x, y)
  for i in range(x, x + CONVERSION_SIZE):
    for j in range(y, y + CONVERSION_SIZE):
      
      if C[i][j] == 0:
        C[i][j] = 1
      else:
        C[i][j] = 0
        

  
  if C == B:
    return count
  else:
    if x == N - CONVERSION_SIZE and y == M - CONVERSION_SIZE:
      return 0
    if x + 1 < M - CONVERSION_SIZE:
      conversion(x + 1, y, C, count)
    if y + 1 < N - CONVERSION_SIZE:
      conversion(x, y + 1, C, count)
  

for i in range(N - CONVERSION_SIZE + 1):
  for j in range(M - CONVERSION_SIZE + 1):
    count = 0
    answer.append(conversion(i, j, A, count))
    
    

print(answer)