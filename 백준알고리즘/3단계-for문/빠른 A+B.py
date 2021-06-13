import sys
input = sys.stdin.readline


def process():
    a, b = map(int, input().split())
    print(a + b)


for i in range(int(input())):
    process()
