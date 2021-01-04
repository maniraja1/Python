import numpy as np
x=np.array([1,2,3,4,5])
#x=np.reshape(x,(5,1))
print(x)
print(x[np.newaxis,:])
print(x[:,np.newaxis])
y=x[np.newaxis,:]
print(y)
print(y[np.newaxis,:])
print(y[:, np.newaxis])
print(y[:,:,np.newaxis])
x=np.array([[[1,2,3],[2,3,4],[3,4,5]], [[4,5,6],[5,6,7],[6,7,8]]])
print(x[0,1,2])