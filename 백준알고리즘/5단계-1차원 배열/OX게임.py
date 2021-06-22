import sys

input = sys.stdin.readline


def process():
    result = input()
    cnt = 0
    res = 0

    for r in result:
        if r == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0

    return res


for i in range(int(input())):
    print(process())
