import math
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

gamma = 1.0
x_0 = 0.0
N = 10**5

def inverse_cauchy(x):
 return gamma*math.tan(math.pi*(x - 0.5)) + x_0

def cauchy(x):
  return 1/(gamma*math.pi * (1 + ( (x-x_0)/gamma )**2) )

 
cau = np.zeros(N) 
for j in range(N):
  cau[j] = random.random()
  cau[j] = inverse_cauchy(cau[j])

plt.figure()
plt.hist(cau, bins = 100, density = True, range=[-15,15])

xx = np.linspace(-15,15,100000)

X = np.zeros(10**5)
for j in range(10**5):
  X[j] = cauchy(xx[j])
plt.plot(xx, X)

mean = 0
var = 0
for j in range(N):
  mean += cau[j]
mean = mean/(N)
for j in range(N):
  var += (cau[j] - mean)**2
var = var/(N - 1) 
print(mean)
print(var)
