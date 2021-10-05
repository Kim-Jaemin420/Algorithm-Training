import sys
import math
input = sys.stdin.readline

S = int(input())
ans = int(math.sqrt(S*2))

while ans**2 + ans > S*2:
  ans -= 1

print(ans)