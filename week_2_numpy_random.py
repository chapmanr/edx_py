import numpy as numpy

#test = numpy.random.normal(1,2,3)
#test = numpy.random.randint(1,5,(2,3))
test = numpy.sum(numpy.random.randint(1,7,(100,10)), axis=0)

print(test)
