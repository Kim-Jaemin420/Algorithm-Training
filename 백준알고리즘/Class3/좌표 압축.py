import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
coordinates = list(map(int, input().split()))
unique_coordinates = set(coordinates)
sorted_coordinates = sorted(unique_coordinates)
count_coordinate = defaultdict(int)

for index, coordinate in enumerate(sorted_coordinates):
  count_coordinate[coordinate] = index

for coordinate in coordinates:
  print(count_coordinate[coordinate], end=" ")