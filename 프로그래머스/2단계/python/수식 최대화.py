def solution(expression):
    answer = 0
    split_m = expression.split('-')
    mul = []
    
    for x in split_m:
      mul.append(x.split('*'))
    return answer

print(solution("100-200*300-500+20"))