import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
sortedNumbers = []
answer = [0] * N

for i in range(N):
  sortedNumbers.append([numbers[i], i])

sortedNumbers.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
  number, index = sortedNumbers[i]
  answer[index] = i

print(*answer)