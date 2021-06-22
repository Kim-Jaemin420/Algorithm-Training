import sys
input = sys.stdin.readline

cnt = 0
remain_num = []
while cnt < 10:
    remain = int(input()) % 42
    if remain not in remain_num:
        remain_num.append(remain)
    cnt += 1

print(len(remain_num))
