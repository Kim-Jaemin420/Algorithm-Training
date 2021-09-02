import sys
input = sys.stdin.readline

a_list, b_list, c_list, d_list = [], [], [], []
N = int(input())

for _ in range(N):
    a, b, c, d = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

ab = dict()

for a in a_list:
    for b in b_list:
        ab[a + b] = ab.get(a + b, 0) + 1

answer = 0
for c in c_list:
    for d in d_list:
        answer += ab.get(-(c + d), 0)
print(answer)
