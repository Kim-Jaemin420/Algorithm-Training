cnt = 1
N = int(input())
sumN = N // 10 + N % 10
newN = N % 10 * 10 + sumN % 10


def process(num):
    sumN = num // 10 + num % 10
    return num % 10 * 10 + sumN % 10


res = process(N)
while True:
    if res != N:
        cnt += 1
        res = process(res)
    else:
        print(cnt)
        break
