import random as r
import numpy as np

n = 100
x_range = 1.5
y_range = 2.0

graph_area = x_range*y_range
total_percentage = np.zeros(n)

for i in range(n):
    under = 0
    total = 10000
    for j in range (total):
        x = r.uniform(0,2)
        y = r.uniform(0,1.5)
        if (y < np.sqrt(np.cos(x)**2+1)):
            under += 1
    total_percentage[i] = (under/total)*graph_area
    
print ("average:", np.mean(total_percentage))
print ("standard deviation:", np.std(total_percentage))