import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
sanggun_list = list(map(int, input().split()))

num_list.sort()

res = []


def check_sanggunCard():
    for s in sanggun_list:
        sp = 0
        ep = N - 1
        while sp <= ep:
            md = (sp + ep) // 2
            if s < num_list[md]:
                ep = 0 if md == 1 else md - 1
            elif s > num_list[md]:
                sp = N if md == N else md + 1
            else:
                res.append(1)
                break
        if sp > ep:
            res.append(0)


check_sanggunCard()

for i, idx in enumerate(res):
    if i == M - 1:
        print(idx)
    else:
        print(idx, end=" ")
