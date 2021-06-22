import sys
input = sys.stdin.readline

N = int(input())


def Hansoo():
    cnt = 0
    for i in range(1, N+1):
        arr = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif arr[1] - arr[0] == arr[2] - arr[1]:
            cnt += 1
    return cnt


print(Hansoo())
