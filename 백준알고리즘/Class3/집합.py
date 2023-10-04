import sys
input = sys.stdin.readline

M = int(input())
S = set()
init_S = set([i for i in range(1, 21)])

for _ in range(M):
  calculate = input().rstrip().split(' ')
  command = calculate[0]
  
  if command == 'add':
    S.add(int(calculate[1]))
  elif command == 'remove':
    S.discard(int(calculate[1]))
  elif command == 'check':
    print(1 if int(calculate[1]) in S else 0)
  elif command == 'toggle':
    try:
      S.remove(int(calculate[1]))
    except:
      S.add(int(calculate[1]))
  elif command == 'all':
    S = init_S
  elif command == 'empty':
    S.clear()