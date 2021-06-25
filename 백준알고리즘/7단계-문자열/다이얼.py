import sys

input = sys.stdin.readline

dial = list(input())
cnt = 0

for d in dial:
    asc = ord(d)

    if 65 <= asc < 68:
        cnt += 3
    elif 68 <= asc < 71:
        cnt += 4
    elif 71 <= asc < 74:
        cnt += 5
    elif 74 <= asc < 77:
        cnt += 6
    elif 77 <= asc < 80:
        cnt += 7
    elif 80 <= asc < 84:
        cnt += 8
    elif 84 <= asc < 87:
        cnt += 9
    elif 87 <= asc < 91:
        cnt += 10

print(cnt)
