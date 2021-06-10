N, M = map(int, input().split())
A, B = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
         3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

whole_name = ""
min_len = min(N, M)

for i in range(min_len):
    whole_name += A[i] + B[i]

whole_name += A[min_len:] + B[min_len:]

lst = [alpha[ord(i) - ord("A")] for i in whole_name]

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        lst[j] += lst[j + 1]

print("{}%".format(lst[0] % 10 * 10 + lst[1] % 10))
