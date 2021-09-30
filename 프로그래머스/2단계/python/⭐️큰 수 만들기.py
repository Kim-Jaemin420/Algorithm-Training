def solution(number, k):
    nums = list(map(int, number))
    ans = []
    
    for num in nums:
      while k > 0 and ans and ans[-1] < num:
        ans.pop()
        k -= 1
      ans.append(num)
    
    if k > 0:
      ans = ans[:k + 1]
    return ''.join(map(str, ans))

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))