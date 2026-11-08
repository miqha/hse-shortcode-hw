from numpy import *

bootci = lambda est, x: quantile([est(random.choice(x, len(x))) for _ in [0] * 999], [.025, .975])