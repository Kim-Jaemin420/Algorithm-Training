from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  n = int(input())
  answer = 1
  clothes = defaultdict(list)
  
  for _ in range(n):
    clothName, clothType = input().split()
    
    clothes[clothType].append(clothName)
  
  for cloth in clothes.values():
    answer *= len(cloth) + 1
  
  print(answer - 1)