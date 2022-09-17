def solution(s):
    sToNumberList = list(map(int, s.split()))
    
    return f'{min(sToNumberList)} {max(sToNumberList)}'


print(solution("1 2 3 4"))
# return "1 4"
print(solution("-1 -2 -3 -4"))
# return "-4 -1"
print(solution("-1 -1"))
# return "-1 -1"