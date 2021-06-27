import sys
input = sys.stdin.readline


def count_sugar():
    N = int(input())
    x = N // 5

    while True:
        check_remain = (N - (x * 5)) % 3
        y = (N - (x * 5)) // 3
        if check_remain == 0:
            return x + y
        else:
            if x == 0:
                break
            x -= 1

    if (N - 3) % 5 == 0:
        return (N - 3) // 5 + 1
    elif (N - 5) % 3 == 0:
        return (N - 5) // 3 + 1
    elif N % 5 == 0:
        return N // 5
    elif N % 3 == 0:
        return N // 3
    else:
        return -1


print(count_sugar())
