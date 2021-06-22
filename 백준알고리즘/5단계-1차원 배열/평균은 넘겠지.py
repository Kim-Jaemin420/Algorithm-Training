import sys

input = sys.stdin.readline


def process():
    score_info = list(map(int, input().split()))
    N = score_info.pop(0)
    mean = sum(score_info) / N
    cnt = 0

    for score in score_info:
        if score > mean:
            cnt += 1

    return '{:.03f}'.format(cnt / N * 100) + '%'


for _ in range(int(input())):
    print(process())
