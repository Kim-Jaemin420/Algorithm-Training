import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dictA = defaultdict(int)
answer = 0

for i in range(n):
    for j in range(i, n):
        dictA[sum(A[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        answer += dictA[T - sum(B[i:j + 1])]

print(answer)
