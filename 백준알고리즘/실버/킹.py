import sys
input = sys.stdin.readline

A_TO_NUMBER = 65
CHESS_SIZE = 8
king, stone, N = input().split()

kingLocation = [int(king[1]) - 1, ord(king[0]) - A_TO_NUMBER]
stoneLocation = [int(stone[1]) - 1, ord(stone[0]) - A_TO_NUMBER]

moveCommands = {
  'R': [0, 1],
  'L': [0, -1],
  'B': [-1, 0],
  'T': [1, 0],
  'RT': [1, 1],
  'LT': [1, -1],
  'RB': [-1, 1],
  'LB': [-1, -1],
}

for _ in range(int(N)):
  command = input().rstrip()
  
  moveCommand = moveCommands[command]
  x, y = moveCommand[0], moveCommand[1]
  
  if 0 <= kingLocation[0] + x < CHESS_SIZE and 0 <= kingLocation[1] + y < CHESS_SIZE:
    if kingLocation[0] + x == stoneLocation[0] and kingLocation[1] + y == stoneLocation[1]:
      if 0 <= stoneLocation[0] + x < CHESS_SIZE and 0 <= stoneLocation[1] + y < CHESS_SIZE:
        stoneLocation = [stoneLocation[0] + x, stoneLocation[1] + y]
      else:
        continue
        
    kingLocation = [kingLocation[0] + x, kingLocation[1] + y]
    
  else:
    continue

print(chr(kingLocation[1] + A_TO_NUMBER) + str(kingLocation[0] + 1))
print(chr(stoneLocation[1] + A_TO_NUMBER) + str(stoneLocation[0] + 1))
  