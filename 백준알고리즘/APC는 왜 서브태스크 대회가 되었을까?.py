N, L, K = map(int, input().split())
diff = []
score = 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    diff.append([sub1, sub2])

for p in diff:
    if p[1] <= L:
        score += 140
    elif p[0] <= L:
        score += 100

print(score)

# 강사님 답
N, L, K = map(int, input().split())
diff = []
easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# hard 문제
ans = min(hard, K) * 140

# easy 문제
if hard < K:
    ans += min(K - hard, easy) * 100

print(ans)
