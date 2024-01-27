import numpy as np
import matplotlib.pyplot as plt

a = 0.5 # 0 < a < 1
b = 3   # ab >= 1 (바이어슈트라스 함수에 필요한 조건)

x = np.arange(-1, 1, 0.00005)
#y = np.zeros(2 * 5 * 10000, dtype="float128")
#y = np.zeros(2 * 5 * 10000, dtype="double")
def sum_w(x):
    y = 0
    for n in range(1000):
        y += np.power(a, n) * np.cos(np.power(b ,n) * np.pi * x)
    return y

def f(x):
    return sum_w(x)
y=f(x)
'''
def f(x):
    return y
for n in range(1000):    
        y += np.power(a, n) * np.cos(np.power(b ,n) * np.pi * x)
    #if n % 100 == 0:
        #print "Now: ", n
'''
p = 0.5
q = f(p)

def ki1(x):

    h = 1e-4 #10^-4

    return (f(x+h)-f(x))/h

def tline1(x, p, q):
    return ki1(p)*(x - p) + q

def ki2(x):

    h = 1e-4 #10^-4

    return (f(x-h)-f(x))/h

def tline2(x, p, q):
    return ki2(p)*(x - p) + q

xrange = np.linspace(p-1, p+1, 2)

plt.grid(True)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.plot(x, y, "black", linewidth=0.1)

plt.scatter(p, q, color='green', s=50)
plt.plot(xrange, tline1(xrange, p, q), 'red', linewidth = 1.5)
plt.plot(xrange, tline2(xrange, p, q), 'blue', linewidth = 2)
plt.show()
#plt.savefig("Weierstrass Function.png", dpi=1200) 사진용