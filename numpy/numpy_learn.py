import numpy as np

## THE BASICS ##

#initializing an array
a = np.array([1,2,3])
print(a)

#2D array
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimention
print(a.ndim)
print(b.ndim)

#get shape (how many itens there are in each dimention)
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#OBS: defining array's size
a = np.array([1,2,3], dtype='int16')

#get size (number of bytes each number occupes)
print(a.itemsize)
print(b.itemsize)

#get total size (number of bytes the whole array occupes)
print(a.nbytes)
print(b.nbytes)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## CHANGES IN THE ARRAY ##

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)

#get especific element [r; c]
print(c[1,5]) #13
print(c[1, -2]) #13]

#get a specific row
print(c[0, :]) #[1,2,3,4,5,6,7]

#get a specific column
print(c[:, 2]) #[3,10]

#running through [start:end:step]
print(c[0, 1:6:2]) #[2,4,6]

#changing element
c[1,5] = 20
print(c)

c[1, :] = 5
print(c)

c[:, 2] = [100, 100]
print(c)

#3D exemple
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
print(d[0,1,1]) #4

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## INITIALIZING DIFFERENT TYPES OF ARRAYS ##

#All 0s matrix
mat = np.zeros((2,3))
print(mat)

#All 1s matrix
mat2 = np.ones((2,2))
print(mat2)

#any other matrix
mat3 = np.full((4,3), 99)
print(mat3)

#full_like matrix
mat4 = np.full_like(c, 4)
print(mat4)
mat5 = np.full_like(d, 6)
print(mat5)

#random decimal numbers
rand1 = np.random.rand(4,2)
print(rand1)

#random Int values (#begin of random, end of random, size of the matrix)
rand2 = np.random.randint(15, 28, size=(2,3))
print(rand2)

#identity matrix
ide = np.identity(3)
print(ide)

#repeating an array
e = np.array([[1,2,3]])
#axis if for select what row you are repeating
e_rep = np.repeat(e, 3, axis=0)
print(e)
print(e_rep)

#testing
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
test = np.ones((5,5))
test[1:4, 1:4] = 0
test[2,2] = 9
print(test)