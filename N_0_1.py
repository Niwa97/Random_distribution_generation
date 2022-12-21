import math
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

def normal(x):
  return 1/(math.sqrt(2 * math.pi)) * math.exp( - x*x/2 )

def polar_metod(N): 
    out = np.zeros(N);
    for j in range(N):
        r = 2
        while r > 1:
            x = random.random() * 2 - 1;
            y = random.random() * 2 - 1;
            r = x**2 + y**2;
        t = math.sqrt((-2) * math.log(r)/r);
        out[j] = x * t;
    
    return out       

Points = polar_metod(10**6) 
plt.figure()
plt.hist(Points, bins = 50, density = True)
xx = np.linspace(-4,4,1000)
X = np.zeros(1000)
for j in range(1000):
  X[j] = normal(xx[j])
plt.plot(xx, X)

mean = 0
var = 0
for j in range(Points.size):
  mean += Points[j]
mean = mean/(Points.size)
for j in range(Points.size):
  var += (Points[j] - mean)**2
var = var/(Points.size - 1) 
print(mean)
print(var)
