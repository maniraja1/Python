from numpy import linalg as LA
from numpy import hstack,array,reshape

m=array([0.65670626, 0.52097334,
       0.07280136, 0.4416958])

print(m)
print(len(m))
print(reshape(m, (len(m), 1)))