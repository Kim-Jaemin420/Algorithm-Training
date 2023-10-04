import heapq
import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().rstrip().split())
dp = [0] * (K + 2)

