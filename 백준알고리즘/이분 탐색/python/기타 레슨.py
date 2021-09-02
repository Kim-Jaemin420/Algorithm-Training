import sys
input = sys.stdin.readline

N, M = map(int, input().split())
video_list = list(map(int, input().split()))


def count(md):
    cnt = 1
    sum = 0
    for v in video_list:
        if sum + v > md:
            cnt += 1
            sum = v
        else:
            sum += v
    return cnt


def solution():
    sp = max(video_list)
    ep = sum(video_list)
    answer = 0

    while sp <= ep:
        md = (sp + ep) // 2
        if count(md) <= M:
            answer = md
            ep = md - 1
        else:
            sp = md + 1
    return answer


print(solution())
