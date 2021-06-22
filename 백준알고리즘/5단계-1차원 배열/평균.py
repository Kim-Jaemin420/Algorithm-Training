N = int(input())
score = list(map(int, input().split()))

rigging_score = []
max_s = max(score)

for s in score:
    rigging_score.append(s / max_s * 100)

print(sum(rigging_score) / N)
