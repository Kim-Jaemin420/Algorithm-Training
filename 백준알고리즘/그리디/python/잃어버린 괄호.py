import sys
input = sys.stdin.readline

expression = input().split('-')

ans = 0
for i in expression[0].split('+'):
    ans += int(i)
for i in expression[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)
