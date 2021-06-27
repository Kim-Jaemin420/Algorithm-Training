import sys
input = sys.stdin.readline

N = int(input())


def prime(N):
    a = [False, False] + [True] * (2 * N - 1)
    primes = []

    for i in range(2, 2 * N + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, 2 * N + 1, i):
                a[j] = False

    return primes


while N != 0:
    a = prime(N)
    b = []
    for i in prime(N):
        if N < i <= 2 * N:
            b.append(i)
    print(len(b))
    N = int(input())
