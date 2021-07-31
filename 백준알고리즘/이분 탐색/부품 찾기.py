import sys
input = sys.stdin.readline

N = int(input())
inventory = list(map(int, input().split()))
M = int(input())
customers = list(map(int, input().split()))

inventory = sorted(inventory)


def binary_search(n):
    sp = 0
    ep = N - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if inventory[md] < n:
            sp = md + 1
        elif inventory[md] > n:
            ep = md - 1
        else:
            return 'yes'

    return 'no'


for c in customers:
    print(binary_search(c))
