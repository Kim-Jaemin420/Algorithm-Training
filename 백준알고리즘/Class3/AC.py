from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = list(input())
  n = int(input())
  stringList = ((input().rstrip())[1:-1]).split(',')
  numbers = deque()
  isReverse = False
    
  for number in stringList:
    if number != '':
      numbers.append(int(number))
  
  if p.count('D') > n and p.count('D') > 0:
    print('error')
    continue
  
  for functionName in p:
    if functionName == 'R':
      isReverse = not isReverse
    
    if functionName == 'D':
      if isReverse:
        numbers.pop()
      else:
        numbers.popleft()
  
  numbers = list(numbers)
  
  if isReverse:
    print(str(numbers[::-1]).replace(' ', ''))
  else:
    print(str(numbers).replace(' ', ''))
