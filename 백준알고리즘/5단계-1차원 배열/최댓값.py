import sys

input = sys.stdin.readline
num = []

while True:
    try:
        num.append(int(input()))
    except ValueError:
        break

max_n = max(num)
print(max_n)
print(num.index(max_n) + 1)
