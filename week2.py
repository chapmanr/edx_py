import numpy as np
import matplotlib.pyplot as plt

def increment(n):
   n += 1
   return n

n = 1
while n < 10:
   n = increment(n)
print(n)


#test for prime
x = 20 
y = not np.any([x%i == 0 for i in range(2, x)])
print(y)


#plt.plot([0,1,2],[0,1,4],"rd-")
#plt.show()

x = np.logspace(0,1,10) 
y = x**2 
plt.loglog(x,y,"bo-")
plt.show()