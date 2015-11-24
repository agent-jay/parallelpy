import multiprocessing as mp


###############
#More control, but 
#interface is harder to use
###############

output= mp.Queue()

def square(x,output):
    output.put((x,x**2))


processes=[mp.Process(target= square, args= (x, output)) for x in range(1,5)]

for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]
print results


################
#Alternate using Pool()
################
pool= mp.Pool(processes=4)
from math import sqrt
from time import time

l=0
h=500000
t= time()
results= map(sqrt, range(l,h))
t1= time()-t
print "Regular map takes ",t1, " seconds"
t= time()
results= pool.map(sqrt, range(l,h))
t2= time()-t
print "Pooled map takes ", t2, " seconds"


print "T2 is this percent faster than t1 ", (t1-t2)*100.0/t1


