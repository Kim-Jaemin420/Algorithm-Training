import sys
input = sys.stdin.readline

T = int(input())


def is_prime(num):
    nums = [False, True] * (num - 1)
    for i in range(2, num + 1):

    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def solution():
    target = int(input())
    if is_prime(target):
        return 0
    else:


for _ in range(T):
    print(solution())
