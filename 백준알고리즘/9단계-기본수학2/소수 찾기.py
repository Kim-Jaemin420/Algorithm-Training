import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
cnt = 0


def find_decimal(num):
    if num == 2:
        return 1
    elif num == 1 or num % 2 == 0:
        return 0
    else:
        for i in range(2, num):
            if num % i == 0:
                return 0
    return 1


for num in num_list:
    if find_decimal(num) == 1:
        cnt += 1

print(cnt)
