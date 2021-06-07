N = int(input())
S = input()
score = 0
bonus = 0

for i in range(N):
    if S[i] == 'X':
        bonus = 0
    elif S[i] == 'O':
        score += i + 1 + bonus
        bonus += 1

print(score)
