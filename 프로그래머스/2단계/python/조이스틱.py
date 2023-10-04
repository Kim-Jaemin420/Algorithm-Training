
def solution(name):
    alpha = {
      'A': 0,
      'B': 1,
      'C': 2,
      'D': 3,
      'E': 4,
      'F': 5,
      'G': 6,
      'H': 7,
      'I': 8,
      'J': 9,
      'K': 10,
      'L': 11,
      'M': 12,
      'N': 13,
      'O': 12,
      'P': 11,
      'Q': 10,
      'R': 9,
      'S': 8,
      'T': 7,
      'U': 6,
      'V': 5,
      'W': 4,
      'X': 3,
      'Y': 2,
      'Z': 1,
    }
    answer = 0
    N = len(name)

    for i in range(N):
      answer += alpha[name[i]]

    idx = name.find('A')
    a_cnt = 0 if idx == -1 else 1
    
    for i in range(N):
      if idx == -1:
        break
      if name[i] == 'A' and i == idx + 1:
        idx = i
        a_cnt += 1
      
    name_s = name.split('A')
    print(name_s, a_cnt)
    

    cnt = (len(name_s[0]) - 1 ) * 2 + N - len(name_s[0]) - a_cnt
    
    return answer + min(cnt, N - 1)

# print(solution("JEROEN"))
# print(solution("BAVADBB"))
# print(solution("ZAAZAAZ"))
# print(solution("ZAAAAZAAZ"))
# print(solution("BBBBAABBB"))
# print(solution("ZZAAAZZ"))
# print(solution("BBBAAB"))#9
print(solution("AABAAAAAAAAABB")) #12
