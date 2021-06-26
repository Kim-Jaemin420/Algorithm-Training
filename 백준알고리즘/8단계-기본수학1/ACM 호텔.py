import sys
input = sys.stdin.readline


def process():
    H, W, N = map(int, input().split())
    num = N // H if N % H == 0 else N // H + 1
    floor = H if N % H == 0 else N % H

    return floor * 100 + num


for _ in range(int(input())):
    print(process())
