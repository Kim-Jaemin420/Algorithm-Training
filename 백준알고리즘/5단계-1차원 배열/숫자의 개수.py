import sys
input = sys.stdin.readline

A, B, C = int(input()), int(input()), int(input())

for i in range(10):
    sum = 0
    for j in str(A*B*C):
        if int(j) == i:
            sum += 1
    print(sum)
