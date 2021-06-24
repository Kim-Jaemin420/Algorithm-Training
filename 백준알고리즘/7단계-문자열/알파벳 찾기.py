import sys
from string import ascii_lowercase

input = sys.stdin.readline
alpha_list = list(ascii_lowercase)

S = input()

for alpha in alpha_list:
    if alpha in S:
        print(S.index(alpha), end=" ")
    else:
        print(-1, end=" ")
