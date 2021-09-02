import sys
input = sys.stdin.readline

N = int(input())
solution_list = list(map(int, input().split()))

solution_list.sort()

sp = 0
ep = N - 1
min_v = float('inf')
answer = []

while sp < ep:
    res = solution_list[sp] + solution_list[ep]

    if abs(res) < min_v:
        answer = [solution_list[sp], solution_list[ep]]
        min_v = abs(res)

    if res >= 0:
        ep -= 1
    else:
        sp += 1

print(answer[0], answer[1])
