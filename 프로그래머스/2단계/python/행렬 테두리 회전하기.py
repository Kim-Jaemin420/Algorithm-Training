def solution(rows, columns, queries):
    answer = []
    graph = [[0] * (columns + 1)]
    for row in range(rows):
      column = [0]
      for c in range(1, columns + 1):
        column.append(row * columns + c)
      graph.append(column)

    while queries:
      query = queries.pop(0)
      x1, y1, x2, y2 = query
      start = graph[x1][y1]
      nums = [start]
      index1, index2 = x1, y1

      while True:
        if index1 < x2 and index2 == y1:
          graph[index1][index2] = graph[index1 + 1][index2]
          nums.append(graph[index1][index2])
          index1 += 1
        if index1 == x2 and index2 < y2:
          graph[index1][index2] = graph[index1][index2 + 1]
          nums.append(graph[index1][index2])
          index2 += 1
        if index1 <= x2 and index2 == y2:
          graph[index1][index2] = graph[index1 - 1][index2]
          nums.append(graph[index1][index2])
          index1 -= 1
        if index1 == x1 and index2 <= y2:
          if index2 == y1 + 1:
            graph[index1][index2] = start
          else:
            graph[index1][index2] = graph[index1][index2 - 1]
            nums.append(graph[index1][index2])
            index2 -= 1
        if len(nums) == ((x2 - x1 + 1) * (y2 - y1 + 1)) - ((x2 - x1 - 1) * (y2 - y1 - 1)):
          break
      
      answer.append(min(nums))

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100  , 97, [[1,1,100,97]]))