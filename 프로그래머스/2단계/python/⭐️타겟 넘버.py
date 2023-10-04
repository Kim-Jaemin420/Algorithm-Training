def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = [[numbers[0], 0], [-numbers[0], 0]]

    while queue:
      tmp, idx = queue.pop()
      idx += 1

      if idx < n:
        queue.append([tmp + numbers[idx], idx])
        queue.append([tmp - numbers[idx], idx])
      else:
        if tmp == target:
          answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))