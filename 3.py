import scipy.optimize as o, math as m

mle = lambda pdf, x, p0: o.fmin(lambda p: -sum(m.log(pdf(z, p)) for z in x), p0)