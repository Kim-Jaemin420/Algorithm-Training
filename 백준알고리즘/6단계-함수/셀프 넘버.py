arr = [i for i in range(1, 10001)]


def generate(num):
    sum = num
    for n in list(str(num)):
        sum += int(n)
    return sum


res = []
for i in arr:
    r = generate(i)
    res.append(r)

for i in res:
    if i in arr:
        arr.remove(i)

for i in arr:
    print(i)
