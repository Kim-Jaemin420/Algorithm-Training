import sys
input = sys.stdin.readline

word = input().upper()

alpha_num = []

for w in word:
    if all(w not in char[0] for char in alpha_num):
        alpha_num.append([w, 1])
    else:
        for a in alpha_num:
            if w == a[0]:
                a[1] += 1

m = ['', 0]

for (alpha, cnt) in alpha_num:
    if cnt > m[1]:
        m = [alpha, cnt]
    elif cnt == m[1]:
        m = ['?', cnt]

print(m[0])
