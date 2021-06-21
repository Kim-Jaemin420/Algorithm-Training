a, b = int(input()), int(input())
b0, b1, b2 = b // 100, b % 100 // 10, b % 100 % 10

print(a*b2)
print(a*b1)
print(a*b0)
print(a*b0*100 + a*b1*10 + a*b2)
