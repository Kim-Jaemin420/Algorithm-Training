N, M = map(int, input().split())

girl_group, mem_group = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    girl_group[team_name] = []
    for j in range(mem_num):
        name = input()
        girl_group[team_name].append(name)
        mem_group[name] = team_name
    girl_group[team_name].sort()

for i in range(M):
    name, sort = input(), int(input())
    if sort == 1:
        print(mem_group[name])
    else:
        for j in girl_group[name]:
            print(j)

# 강사님 답
N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_team = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
