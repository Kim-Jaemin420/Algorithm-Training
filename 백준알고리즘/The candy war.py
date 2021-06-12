def process():
    N, candy_list = int(input()), list(map(int, input().split()))
    num = 1
    print('N', N)
    i = 0
    while True:
        print(candy_list)
        if candy_list[i] % 2 == 1:
            candy_list[i] = (candy_list[i] + 1) // 2
            if i == N - 1:
                candy_list[0] = candy_list[i] + candy_list[0]
                num += 1
                i = -1
            else:
                candy_list[i + 1] = candy_list[i] + candy_list[i + 1]
        elif candy_list[i] % 2 == 0:
            candy_list[i] //= 2
            if i == N - 1:
                candy_list[0] = candy_list[i] + candy_list[0]
                num += 1
                i = -1
            else:
                candy_list[i + 1] = candy_list[i] + candy_list[i + 1]
            if i == 0:
                print('첫번째 요소', candy_list[i], candy_list[i + 1])
        i += 1

        if num == 8:
            break

    return num


for i in range(int(input())):
    print(process())


# 강사님 답
def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx + 1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0

    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)

    return cnt


for i in range(int(input())):
    print(process())
