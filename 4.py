import numpy as n, scipy.stats as s

x = n.loadtxt([input()])
m, _, a, v, *z = s.describe(x, 0, 1, 0)

print(a, n.median(x))
for i in v - v/m, v:
    print(i, i**.5)
print(*z)
