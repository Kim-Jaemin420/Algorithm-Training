# 이전에 시간초과 나왔던 문제
# 이진탐색을 이용해서 풀어야 했던 문제였다.
N, A = int(input()), list(map(int, input().split()))
M, M_list = int(input()), list(map(int, input().split()))

A.sort()


for m in M_list:
    sp = 0
    ep = N - 1
    while sp <= ep:
        md = (sp + ep) // 2
        if m == A[md]:
            print(1)
            break
        elif m > A[md]:
            sp = md + 1
        elif m < A[md]:
            ep = md - 1
    if sp > ep:
        print(0)


# 강사님 풀이
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()
for i in list(map(int, input().split())):
    print(A.get(i, 0))
