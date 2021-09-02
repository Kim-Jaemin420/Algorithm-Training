import sys
input = sys.stdin.readline


def process():
    x, y = map(int, input().split())
    cnt = 1
    mv = 1
    current = x
    y -= 1

    while current < y:
        current += mv
        mv += 1
        cnt += 1
    print(cnt)


for _ in range(int(input())):
    print(process())
