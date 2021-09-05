import numpy as np
np.__version__
import matplotlib.pyplot as plt
# x vector contains x1,x2,x3 
x = np.array([-1,2,4])

# y vector contains y1,y2,y3 
y=np.array([2,3,-3])


x = x +1
y = y - 2
coord = ['A','B','C']

plt.quiver([0, 0], [0, 0],[3, 5], [ 1, -5],color=['g','r'], angles='xy', scale_units='xy', scale=1)
plt.xlim(-5, 7)
plt.ylim(-7, 5)

plt.scatter([0,3,5], [0, 1, -5],color='k')

for i in range(3):
  plt.text(x[i],y[i]+0.5,'{}({},{})'.format(coord[i],x[i],y[i]))


plt.text(1.5,1,'B-A')
plt.text(2.5,-2,'C-A')

plt.title('Vector Representation of triangle')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid()
plt.plot([3,5],[1,-5],'b--')
plt.show()
BA= np.array([3,1])
CA = np.array([5,-5])
def crossproduct(a1,a2,a3,b1,b2,b3):
  P = np.array([[0,-a3,a2],[a3,0,-a1],[-a2,a1,0]])
  Q=np.array([b1,b2,b3])
  return np.matmul(P,Q)

BA_X_CA = crossproduct(3,1,0,5,-5,0)
Area = (1/2)*(np.sqrt(np.dot(BA_X_CA,BA_X_CA)))

print('Area of triangle is {:.2f} square units.'.format(Area))