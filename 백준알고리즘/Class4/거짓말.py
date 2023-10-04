import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]

truth = set(truth)
parties = []
liable = [True] * M

for _ in range(M):
  members = list(map(int, input().split()))[1:]
  parties.append(members)

for _ in range(M):
  for index, party in enumerate(parties):
    if truth.intersection(party):
      liable[index] = False
      truth = truth.union(set(party))
      
print(liable.count(True))