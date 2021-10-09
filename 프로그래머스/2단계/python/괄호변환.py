def check_correct(w):
    if w[0] == '(':
        return True
    else:
        return False

def split_uv(p):
  tmp = []
  open_cnt = 0
  close_cnt = 0

  for i in range(len(p)):
    if p[i] == '(':
      open_cnt += 1
    else:
      close_cnt += 1
    if open_cnt == close_cnt:
      tmp.append(p[:i + 1])
      tmp.append(p[i + 1:])
      break
  return tmp

def solution(p):
    answer = ''
    w = [split_uv(p)]
    
    while w[-1][1] != '':
      w.append(split_uv(w[-1][1]))
    
    while len(w) != 0:
      tmp = w.pop()
      
      if check_correct(tmp[0]):
        if tmp[1] == '':
          answer += tmp[0]
        else:
          answer = tmp[0] + answer
      else:
        s = '(' + answer + ')'
        if len(tmp[0]) > 2:
          for i in range(1, len(tmp[0]) - 1):
            if tmp[0][i] == '(':
              s += ')'
            else:
              s += '('
        answer  = s
            
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))