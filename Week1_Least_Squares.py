import numpy as np 
from numpy.linalg import inv
import matplotlib.pyplot as plt

I = np.array([[0.2, 0.3, 0.4, 0.5, 0.6]]).T
V = np.array([[1.23, 1.38, 2.06, 2.47, 3.17]]).T
plt.scatter(I,V)
plt.xlabel('Current (A)')
plt.ylabel('VOltage (V)')
plt.grid(True)
plt.show()

# Define the H matrix - what does it contain?
H = np.ones((5,2))
print(H)
H[:,0] = I.T
print(H)

# Now estimate the resistance parameter.
R_ls =  inv(H.T.dot(H)).dot(H.T.dot(V)) 

I_line = np.arange(0, 0.8, 0.1).reshape(8, 1)
V_line = R_ls[0,0]*I_line

plt.scatter(I, V)
plt.plot(I_line, V_line)
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()
