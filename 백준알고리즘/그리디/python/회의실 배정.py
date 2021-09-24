import sys
input = sys.stdin.readline

N = int(input())
conf_times = []

for _ in range(N):
    conf_times.append(tuple(map(int, input().split())))

conf_times.sort(key=lambda x: (x[1], x[0]))

start = [(0, 0)]
for time in conf_times:
    if time[0] >= start[-1][1]:
        start.append(time)

print(len(start) - 1)
