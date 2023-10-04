from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
graph = defaultdict(list)

for _ in range(N):
  node, left, right = input().rstrip().split()
  graph[node].append(left)
  graph[node].append(right)

def preOrderTraverse(node):
  if node == '.': return
  
  print(node, end="")
  preOrderTraverse(graph[node][0])
  preOrderTraverse(graph[node][1])

def inOrderTraverse(node):
  if node == '.': return
  
  inOrderTraverse(graph[node][0])
  print(node, end="")
  inOrderTraverse(graph[node][1])
  
def postOrderTravers(node):
  if node == '.': return
  
  postOrderTravers(graph[node][0])
  postOrderTravers(graph[node][1])
  print(node, end="")
 
preOrderTraverse('A')
print()
inOrderTraverse('A')
print()
postOrderTravers('A')
print()