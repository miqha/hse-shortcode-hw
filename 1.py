import numpy as n, seaborn as s, matplotlib.pyplot as p
a=[*map(float,input().split())]
print(n.quantile(a,float(input()))); s.ecdfplot(a); p.show()
