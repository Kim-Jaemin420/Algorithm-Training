import sys
input = sys.stdin.readline

N, K = map(int, input().split())
correct_nums = list(map(int, input().split()))

sp = 0
ep = sum(correct_nums) + 1


def devide(n):
    cnt = 0
    total = 0

    for num in correct_nums:
        total += num
        if total >= n:
            cnt += 1
            total = 0
    return cnt


while sp + 1 < ep:
    md = (sp + ep) // 2

    if devide(md) >= K:
        sp = md
    else:
        ep = md

print(sp)
