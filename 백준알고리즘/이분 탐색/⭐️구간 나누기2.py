import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))


def devide(v):
    max_v = nums[0]
    min_v = nums[0]
    cnt = 1

    for i in range(1, N):
        max_v = max(max_v, nums[i])
        min_v = min(min_v, nums[i])

        if max_v - min_v > v:
            cnt += 1
            max_v = nums[i]
            min_v = nums[i]
    return cnt


sp, ep = 0, max(nums)
res = 0

while sp <= ep:
    md = (sp + ep) // 2

    if devide(md) <= M:
        ep = md - 1
        res = md
    else:
        sp = md + 1

print(res)
