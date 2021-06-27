import sys
input = sys.stdin.readline


def process(k, n):
    if k == 0:
        return [i for i in range(1, n + 1)]
    else:
        l = process(k - 1, n)
        return [sum(l[:i]) for i in range(1, n + 1)]


for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(process(k, n)[n - 1])
