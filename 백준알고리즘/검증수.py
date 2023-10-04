import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
print(sum([number ** 2 for number in numbers]) % 10)