import heapq
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[0] * numbers[-1])
