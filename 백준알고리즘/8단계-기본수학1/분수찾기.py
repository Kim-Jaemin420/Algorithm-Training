import sys
input = sys.stdin.readline

X = int(input())


def get_fraction(X):
    i = 1
    sum = 1

    while sum < X:
        i += 1
        sum += i

    target_list = []

    for x in range(i, 0, -1):
        target_list.append((x, i + 1 - x))
    if i % 2:
        return target_list[-(sum - X + 1)]
    else:
        return target_list[sum - X]


a, b = get_fraction(X)
print(str(a)+'/'+str(b))
