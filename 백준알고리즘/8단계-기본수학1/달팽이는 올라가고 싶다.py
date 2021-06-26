import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())


def get_snail_day():
    share = (V-A) // (A - B)
    remain = (V-A) % (A - B)

    if remain == 0:
        return share + 1
    else:
        return share + 2


print(get_snail_day())
