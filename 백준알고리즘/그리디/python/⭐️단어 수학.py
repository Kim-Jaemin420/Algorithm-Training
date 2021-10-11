import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
num = 9
alpha = {}
res = 0

words.sort(key=lambda i: -len(i))

for i in range(N):
  for j in range(len(words[i])):
    if words[i][j] in alpha:
      alpha[words[i][j]] += 10**(len(words[i]) - j - 1)
    else:
      alpha[words[i][j]] = 10**(len(words[i]) - j - 1)

sort_alpha = sorted(alpha.items(), reverse=True, key=lambda x: x[1])

for item in sort_alpha:
  res += item[1] * num
  num -= 1

print(res)