import matplotlib.pyplot as plot
import numpy as nump
nump.random.seed(1)
data = nump.random.normal(loc = 20,scale = 2,size = 1000)

plot.hist(data, color = "red", ec = "orange")
plot.show()