import numpy as np
'''Write code to create a 1D NumPy array of integers from 1 to 10.'''
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)

'''How do you access the 5th element in a NumPy array? Try with an array you create.'''
print(arr[4])

'''How can you find the shape and size of a 2D NumPy array? Create a 3x4 array and print its shape and size.'''
arr1 = np.array([[1,2],[1,2]])
print(arr1.shape)
print(arr1.size)
arr3 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(arr3.shape)
print(arr3.size)

'''Given an array arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), how can you slice and retrieve only the elements from index 2 to 5?'''
arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr4[2:6])

'''Create an array of 12 elements (from 1 to 12) and reshape it into a 3x4 matrix.'''
arr5 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshapedarr= arr5.reshape(3,4)
print(reshapedarr)

'''Perform element-wise addition, subtraction, multiplication, and division on two arrays of size 3x3.'''
arr6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr7 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.add(arr6,arr7))
print('\n')
print(np.subtract(arr6,arr7))
print('\n')
print(np.multiply(arr6,arr7))
print('\n')
print(np.divide(arr6,arr7))
print('\n')
print(np.divmod(arr6,arr7))

'''Use np.arange() to generate an array of numbers between 0 and 20, spaced by 2.
Use np.linspace() to generate an array of 10 numbers evenly spaced between 0 and 1.'''
arr8 = np.arange(0,20,2)
arr9 = np.linspace(1,10,num=10,retstep=True)
print(arr8)
print(arr9)
