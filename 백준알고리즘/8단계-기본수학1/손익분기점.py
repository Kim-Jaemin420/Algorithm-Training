import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def get_break_point():
    if C - B <= 0:
        return -1
    else:
        break_point = A // (C - B) + 1
        return break_point


print(get_break_point())
