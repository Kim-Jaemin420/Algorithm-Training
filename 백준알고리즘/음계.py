import sys
input = sys.stdin.readline

sounds = list(map(int, input().split()))

if sounds == sorted(sounds):
  print('ascending')
elif sounds == sorted(sounds)[::-1]:
  print('descending')
else:
  print('mixed')