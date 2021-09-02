import sys
input = sys.stdin.readline

X, Y = map(int, input().rsplit())
Z = Y * 100 // X
answer = sys.maxsize

sp = 0
ep = 1000000000

while sp <= ep:
    md = (sp + ep) // 2

    curr_vic = (Y + md) * 100 // (X + md)

    if curr_vic > Z:
        answer = min(md, answer)
        ep = md - 1
    else:
        sp = md + 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
