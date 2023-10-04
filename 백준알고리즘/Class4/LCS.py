import sys
input = sys.stdin.readline

S1, S2 = input().strip(), input().strip()
matrix = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i in range(1, len(S1) + 1):
  for j in range(1, len(S2) + 1):
    if S1[i - 1] == S2[j - 1]:
      matrix[i][j] = matrix[i - 1][j - 1] + 1
    else:
      matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])


