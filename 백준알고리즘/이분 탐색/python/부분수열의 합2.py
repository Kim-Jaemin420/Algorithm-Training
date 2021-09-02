import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()


def solution():
    ans = 0
    for i in range(N):
        if num_list[i] == S:
            ans += 1
            break
        else:
            sp = i + 1
            ep = N - 1
            sum = num_list[i]
            while sp <= ep:
                md = (sp + ep) // 2
                sum += num_list[md]

                if sum > S:
                    ep = md - 1
                elif sum < S:
                    sp = md + 1
                else:
                    ans += 1
                    break
    return ans


print(solution())
