
# All the different ways to create an array
https://app.pluralsight.com/guides/different-ways-create-numpy-arrays

# Building a NXN matrix or norm/distances from a nX2 matrix
def pairwise_dist(X):
    r, c = X.shape
    temp=[]
    for i in range(r):
        x=np.linalg.norm(X - X[i], axis=1)
        temp.append(np.reshape(x, (r,1)))
    D = np.hstack(temp)
    print(D)
    return D

# Building a N dimensional random matrix
np.random.rand(10, 1)

# Building outer product of two vectors
np.outer(m, m)

# Square a matrix
D_2 = D**2

#Identity matrix
np.eye(D.shape[0])

#Return an array of zeros with the same shape and type as a given array.
V = np.zeros_like(V_init)

# Build a diagonal matrix with diaganol values from original matrix
np.diag(np.diag(M))

#Multiple matrix and its transpose
import scipy.sparse as sp
X = sp.csr_matrix(X)
display(X.dot(X.T).toarray())

#first nonzero element in an array
y.nonzero()

#Understand difference betwen np.multiply and np.dot
#np.multiply carries element wise multiplication
#np.dot carries matrix multiplication
#Trick with matrix multiply is if you reshape the matrix to be a vector then multiple and dot product should
# yield the same result
np.multiply
np.dot
# this will perform dot product
* # this will carry out element wise multiplication

#np.arrange
arr_1d_bigger = np.arange(24)

#np.reshape 2d
arr_1d_bigger = np.arange(24)
arr_2d=np.reshape(arr_1d_bigger,(6,4))

#np.reshape 3d

#np array from data frame (matrix)
travel_matrix = np.array(travel_matrix)

#Round trip calculation
round_trip = travel_matrix + travel_matrix.T

# Find correlation coefficient
np.corrcoef(col1, col2)[0,1]



