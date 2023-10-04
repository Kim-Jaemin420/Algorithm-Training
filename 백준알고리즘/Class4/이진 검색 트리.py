from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = defaultdict(list)
root = int(input())
graph[root] = [0, 0]
roots = [root]

while True:
  try:
    node = int(input())
    
    graph[node] = [0 , 0]
    
    if node < roots[-1]:
      graph[roots[-1]][0] = node
      roots.append(node)
    else:
      temp = 0
      while roots and roots[-1] <= node:
        temp = roots.pop()
      roots.append(node)
      graph[temp][1] = node
    print(graph)
    
  except:
    break

def postOrderTraverse(node):
  if node == 0:
    return
  
  postOrderTraverse(graph[node][0])
  postOrderTraverse(graph[node][1])
  print(node)
  
postOrderTraverse(root)