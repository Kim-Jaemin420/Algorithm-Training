def dfs(z, x, y, places):
  dx_1 = [-1, 1, 0, 0]
  dy_1 = [0, 0, -1, 1]
  dx_2 = [-2, -1, -1, 0, 0, 1, 1, 2]
  dy_2 = [0, -1, 1, -2, 2, -1, 1, 0]

  for i in range(4):
    nx = x + dx_1[i]
    ny = y + dy_1[i]
    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
      continue
    else:
      if places[z][nx][ny] == 'P':
        return 0
  
  for i in range(8):
    nx = x + dx_2[i]
    ny = y + dy_2[i]

    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
      continue
    else:
      if places[z][nx][ny] == 'P':
        if i == 0 and 0 <=nx + 1 < 5:
          if places[z][nx + 1][ny] != 'X':
            return 0
        if i == 1 and (0 <= ny + 1 < 5 and 0 <= nx + 1 < 5):
          if places[z][nx][ny + 1] != 'X' or places[z][nx + 1][ny] != 'X':
            return 0
        if i == 2 and (0 <= ny - 1 < 5 and 0 <= nx + 1 <= 5):
          if places[z][nx + 1][ny] != 'X' or places[z][nx][ny - 1] != 'X':
            return 0
        if i == 3 and 0 <= ny + 1 < 5:
          if places[z][nx][ny + 1] != 'X':
            return 0
        if i == 4 and 0 <= ny - 1 < 5:
          if places[z][nx][ny - 1] != 'X':
            return 0
        if i == 5 and  (0 <= nx - 1 < 5 and 0 <= ny + 1 < 5):
          if places[z][nx - 1][ny] != 'X' or places[z][nx][ny + 1] != 'X':
            return 0
        if i == 6 and (0 <= nx + 1 < 5 and 0 <= ny + 1 < 5):
          if places[z][nx + 1][ny] != 'X' and places[z][nx][ny + 1] != 'X':
            return 0
        if i == 7 and 0 <= nx - 1 < 5:
          if places[z][nx - 1][ny] != 'X':
            return 0
  
  return 1



def solution(places):
    answer = [1, 1, 1, 1, 1]

    for i in range(5):
      for j in range(5):
        for k in range(5):
          if places[i][j][k] == 'P':
            if dfs(i, j, k, places) == 0:
              answer[i] = 0
              break

    return answer

print(solution([
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
  ]))