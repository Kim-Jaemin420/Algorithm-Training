import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

INF = 1e9
GUITAR_STRING = 6

N, M = map(int, input().split())
setPrice, singlePrice = INF, INF

for _ in range(M):
  setStringPrice, singleStringPrice = map(int, input().split())
  
  setPrice = min(setPrice, setStringPrice)
  singlePrice = min(singlePrice, singleStringPrice)

totalPrice = 0
if N > GUITAR_STRING:
  if N % GUITAR_STRING == 0:
    totalPrice = min(N // GUITAR_STRING * setPrice, N * singlePrice)
  else:
    totalPrice = min((N // GUITAR_STRING * setPrice + N % GUITAR_STRING * singlePrice), (N // GUITAR_STRING + 1) * setPrice, N * singlePrice)
else:
  totalPrice = min(setPrice, singlePrice * N)
  
print(totalPrice)