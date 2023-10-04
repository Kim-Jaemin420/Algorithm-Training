from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def operatorD(number):
  if number * 2 > 9999:
    return number * 2 % 10000
  return number * 2

def operatorS(number):
  if number == 0:
    return 9999
  return number - 1

def operatorL(number):
  return (number % 1000) * 10 + number // 1000

def operatorR(number):
  return (number % 10) * 1000 + (number // 10)

def bfs(start, target):
    queue = deque()
    visited = set()
    queue.append([start, ''])
    visited.add(start)
    
    while queue:
      current, operators = queue.popleft()
      
      if current == target:
        print(operators)
        return

      temp = operatorD(current)
      if temp not in visited:
        queue.append([temp, operators + 'D'])
        visited.add(temp)
      
      temp = operatorS(current)
      if temp not in visited:
        queue.append([temp, operators + 'S'])
        visited.add(temp)
      
      temp = operatorL(current)
      if temp not in visited:
        queue.append([temp, operators + 'L'])
        visited.add(temp)
      
      temp = operatorR(current)
      if temp not in visited:
        queue.append([temp, operators + 'R'])
        visited.add(temp)
      

for _ in range(T):
  A, B = map(int, input().split())

  bfs(A, B)
  
    