from numpy import *
from scipy.stats import norm, t

'''
k is a mode of f:
    k = 1: normal
    k = 2: student
    k = 3: Hoeffding
p: confidence width
a, b: limits of distribution
'''

f = lambda x, p, k, a=0, b=1: mean(x) + array([-1, 1]) / sqrt(len(x)) * (
    (b - a) * sqrt(log(2 / (1 - p)) / 2) if k == 3 
    else
        # fixed std
        std(x, ddof=1) * (
            norm if k == 1 else t(len(x) - 1)
        ).ppf((1 + p) / 2)
)
