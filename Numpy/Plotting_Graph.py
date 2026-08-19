
# Here we have to do the plotting graph using numpy and matplolib
# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as ply 


# Creating an array 
# Graph of the Line pass through origin
x = np.linspace(-10,10,100)
print(x)
y = x

# Plot the graph
ply.plot(x,y)
ply.show()

# Draw the graph of the parabola  equations 

x1 = np.linspace(-20,20,50)
print(x1)

y1 = x1**2
ply.plot(x1,y1)
ply.show()

# Draw the graph of the sinx 
x2 = np.linspace(-15,15,60)
print(x2)

y2 = np.sin(x2)
ply.plot(x2,y2)
ply.show()

# Draw he graph of the cosx 
x3 = np.linspace(-30,30,400)
print(x3)

y3 = np.cos(x3)
ply.plot(x3,y3)
ply.show()

# PLot the graph of the xlogx
x4 = np.linspace(-10,10,10)
print(x4)

# make the formula for the xlogx
y4 = x4*(np.log(x4))
ply.plot(x4,y4)
ply.show()

# Plot the graph of the sigmoid 
x5 = np.linspace(-20,20,200)
print(x5)

y5 = 1/(1+np.exp(-x5))
ply.plot(x5,y5)
ply.show()
