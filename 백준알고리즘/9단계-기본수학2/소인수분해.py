import sys
input = sys.stdin.readline

decimals = []
divisors = []
div_prime = []


def find_decimal():
    N = int(input())

    for i in range(2, N):
        if N % i == 0:
            divisors.append(i)
    print(divisors)


def get_prime():
    print(divisors)
    for i in divisors:
        if i > 3:

            for j in range(2, i):
                print(i)
                if i % j == 0:
                    divisors.remove(i)
                    break
        div_prime.append(i)

    print('prime', divisors)


find_decimal()
get_prime()
