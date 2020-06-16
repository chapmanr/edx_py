import math
import random

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors  
    #print(x)  
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    y=[]
    for i in range(n):
        win = x[i:i+width]
        #print(win)
        y.append(sum(win)/width)
    return y

x = [0,10,5,3,1,5]
print("x before ", x)
avg = moving_window_average(x, 1)
print("x after ", x)
print("mov win avg = ", avg)
sum_avg = sum(avg)
print("sum mov win avg", sum_avg)

random.seed(1)

def rand():
    # a uniform value between -1 and 1
    return random.uniform(0.0, 1.0)

R = 1000
rv = []
for i in range(R):
    rv.append(rand())

Y={}
Y[0]=rv
for nn in range(1,9):
    #print(nn)
    Y[nn]=moving_window_average(rv, nn)
print("Value at nn = 5 10th element = ", Y[5][9])

min_max_list =[]
for sig in Y:
    min_max_list.append(max(Y[sig]) - min(Y[sig]))
print(min_max_list)
