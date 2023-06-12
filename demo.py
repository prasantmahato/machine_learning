import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

def fx(x,a, b,c):
    return a*x*x + b*x + c

def gx(x,c):
    return c*x*x

# make data
# 3n^2 - 100n + 6
lim = 200

# fx
a=3
b=(-100)
c=6

# gx
c1=2

y1 = []
y2 = []
for i in range(0, lim):
    y1.append(fx(i, a, b,c))
    y2.append(gx(i,c1))
    
x1=[x for x in range(0, lim)]
x2=x1

# plot
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()