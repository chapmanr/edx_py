import math
import random

random.seed(1) # Fixes the seed of the random number generator.

def rand():
    # a uniform value between -1 and 1
    return random.uniform(-1.0, 1.0)


def distance(v1,v2):
    if type(v1) == tuple and type(v2) == tuple:
        if len(v1)==2 and len(v2) == 2:
            x_dist = abs(v1[0]-v2[0])
            y_dist = abs(v1[1]-v2[1])
            x_squ = x_dist**2
            y_squ = y_dist**2
            return math.sqrt(x_squ + y_squ)
        else:
            print("incorrect number of elements in tuple")
    else:
        print("incorrect params to distance use tuples")

print(distance((0,0), (1,1)))

def in_circle(x, origin=(0,0)):
    if(distance(x, origin)<=1):
        return True
    return False

print(in_circle((1,1)))

R=10000
tf_list = []

for i in range(R):
    tf_list.append(in_circle((rand(), rand())))

true_count = 0
for tf in tf_list:
    if(tf==True):
        true_count = true_count + 1

ratio_tf = true_count / R
print("Ratio= ", ratio_tf)

print (abs((math.pi / 4)-ratio_tf))