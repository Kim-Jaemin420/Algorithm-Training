import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
d = N // 5
r = N % 5

while True:
    if r == 0:
        cnt += N // 5
        break
    elif (N - d * 5) % 3 != 0:
        d -= 1
    elif d > 0 and (N - d * 5) % 3 == 0:
        cnt += d + ((N - d * 5) // 3)
        break
    elif N % 3 == 0:
        cnt += N // 3
        break
    else:
        cnt -= 1
        break


print(cnt)

########################
# 다른 사람 풀이
########################
n = int(input())

count = 0
while True:
    if n % 5 == 0:
        count += n//5
        print(count)
        break

    count += 1
    n -= 3
    if n < 0:
        print(-1)
        break
