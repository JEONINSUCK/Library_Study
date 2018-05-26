import numpy as np

arr = np.arange(1,6)

print(arr ** 0.5)

arr2 = np.array([np.sum(arr),np.average(arr),np.min(arr),np.max(arr)])
print(arr2)

b = np.reshape(arr2,[4,1])
print(b)
print("*"*40)

arr2 = np.reshape(arr2,[1,4])
arr3 = (np.transpose(arr2))
print(arr3)

print(np.matmul(arr2,arr3))
