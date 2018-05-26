import numpy as np

"""
product = np.array([300,80])

sales = np.array([4,3])

# 배열의 요소끼리 곱한다.
_result = np.multiply(product,sales)

print("_result: ",_result)

result = np.sum(_result)

print("총금액: ",result)

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])
A = np.reshape(a,[2,2])
B = np.reshape(b,[2,2])

print("\n행렬 A")
print(A)

print("\n 행렬 B")
print(B)

result3_1 = np.matmul(A,B)
result3_2 = np.matmul(B,A)

print("\n행렬 result3_1")
print(result3_1)

print("\n행렬 result3_2")
print(result3_2)

b = np.reshape(b, [1,4])
a = np.reshape(a, [1,4])
b2 = np.transpose(b)
print(b2)
print("*" *40)
result = np.matmul(a,b2)
print(result)


data = np.random.randn(2,3)
print(data)
print("*" * 40)

print(data *10)
print("*" * 40)

print(data + data)
print("*" * 40)

print(data.shape)
print("*" * 40)

print(data.dtype)
print("*" * 40)

### 행 과 열 각각 구하기

print("행수: ", data.shape[0])
print("*" * 40)

print("열수: " ,data.shape[1])
print("*" * 40)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

print(arr2)
print()

print(arr2.ndim)
print()

print(arr2.shape)
print()

print(arr2.dtype)
print()

print(np.zeros(3))
print()

print(np.zeros((3,6)))
print()

print(np.empty((2,3,2)))
print()

print(np.arange(4))
print()

arr1 = np.array([1,2,3,4], dtype=np.float64)
print(arr1.dtype)
print()
arr1 = np.array([1,2,3], dtype = np.int32)
print(arr1.dtype)
print()

arr2 = np.array([1,2,3,4,5])
print(arr2.dtype)
print()

float_arr = arr2.astype( np.float64)
print(float_arr.dtype)

arr3 = np.array([1.1,2.7,3.6])
print(arr3)
print()

int_arr4 = arr3.astype(np.int32)
print(int_arr4.dtype)
"""

list1 = [0,1,2,3,4,5,6,7,8,9]

arr1 = np.array(list1)
print(arr1)
print()

print(arr1[5:8])

arr_slice = arr1[5:8]
arr_slice[1] = 100
print(arr1)
print()

list2 = [[0,1,2],[3,4,5],[6,7,8]]
arr2d = np.array(list2)

print(arr2d[2])
print()

print(arr2d[0][2])
print()

print(arr2d[0,2])
print()

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print()

print(arr3d[0])
print()

old_values = arr3d[0].copy()
arr3d[0] = 100
print(arr3d)
print()

arr3d[0] = old_values
print(arr3d)
print()

