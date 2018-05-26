import numpy as np

arr = np.array([[1,2,4],[4,5,6]])
print('\n # 배열의 타입 확인 : ', type(arr))

print(arr[0][0],arr[1][1],arr[1][2])
print("*" * 40)

print("Rank: ", arr.ndim)
print("*" * 40)

print(arr.shape)
print("*" * 40)

arr[0] = 5
print(arr)
print("*" * 40)

print(arr.dtype)
