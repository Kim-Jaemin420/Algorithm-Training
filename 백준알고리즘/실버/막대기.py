import sys
input = sys.stdin.readline

MAX_SIZE = 64
X = int(input())
answer = 0

barSize = MAX_SIZE
while X > 0:
  if X < barSize:
    barSize //= 2
  else:
    X -= barSize
    answer += 1
    
print(answer)
  