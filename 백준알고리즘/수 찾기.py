import sys
# 시간 초과

N, A = int(input()), list(map(int, input().split()))

M, B = int(input()), list(map(int, input().split()))


for i in B:
    if i in A:
        print(1)
    else:
        print(0)


N, A = int(sys.stdin.readline()), set(map(int, sys.stdin.readline().split()))

M, B = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

# 강사님 풀이
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()
for i in list(map(int, input().split())):
    print(A.get(i, 0))
    # print(1 if i in A else 0)
