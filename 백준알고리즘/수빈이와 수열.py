# -*- coding: utf-8 -*-

N, list_b = input(), list(map(int, input().split()))
list_a = []

for i in range(len(list_b)):
    list_a.append(list_b[i] * (i + 1) - sum(list_a[0:i]))

for i in list_a:
    print(i, end=" ")
