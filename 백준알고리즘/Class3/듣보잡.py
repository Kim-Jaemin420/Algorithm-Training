import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

names = defaultdict(int)
never_seen_heard = []

for _ in range(N + M):
  name = input().rstrip()
  
  if names[name] > 0:
    never_seen_heard.append(name)
  else:
    names[name] += 1

never_seen_heard.sort()
print(len(never_seen_heard))
for person in never_seen_heard:
  print(person)
