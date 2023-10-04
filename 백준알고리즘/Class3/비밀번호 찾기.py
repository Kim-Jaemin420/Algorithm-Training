import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
pw_infomation = defaultdict(str)

for _ in range(N):
  email, pw = input().split()
  pw_infomation[email] = pw

for _ in range(M):
  email = input().rstrip()
  print(pw_infomation[email])