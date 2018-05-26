from pandas import Series
import pandas
myseries = Series([10,20,30,40])
print(myseries)

print("*" * 40)
print(myseries.values)
print("*" * 40)
print(myseries.index)
print("*" * 40)

myseries2 = Series([10,20,30,40], index=['강감찬','을지문덕','세종대왕','이순신'])

print(myseries2)
myseries2.name = '호호호'
myseries2.index.name = 'abcd'
print(myseries2)

print("*" * 40)
print(myseries2['세종대왕'])
print("*" * 40)
print(myseries2[myseries2<30])
print("*" * 40)
print(myseries * 2)
print("*" * 40)
print(myseries2)
print("*" * 40)
print('이순신' in myseries)
print("*" * 40)
Data = {"서울":2000,"부산":3000,"울산":4000,"광주":5000}

myseries3 = Series(Data)
print(myseries3)
print("*" * 40)
print(pandas.isnull(myseries2))
print(myseries2 + myseries3)


##############################################################

import numpy as np

Myseries = Series( (np.arange(9) + 1) * 10, \
 index=[['강감찬', '강감찬', '강감찬', '김유신', '김유신', '김유신', '이순신', '이순신', '이순신'], \
 ['갑', '을', '병', '갑', '을', '병', '갑', '을', '병']])

print(Myseries.index)
print("*" * 40)
print(Myseries)
print("*" * 40)
print(Myseries['강감찬'])
print("*" * 40)
print(Myseries[:,"을"])
print("*" * 40)
print(Myseries.unstack())
print("*" * 40)
print(Myseries.unstack(0))
print("*" * 40)
print(Myseries.unstack(1))
print("*" * 40)
print(Myseries.unstack().stack())
print("*" * 40)


myframe = pandas.DataFrame( (np.arange(12).reshape(4, 3)), \
 index=[['강감찬', '강감찬', '이순신', '이순신'], \
 ['갑', '을', '갑', '을']], \
 columns = [['서울', '부산', '서울'], \
 ['Green', 'Red', 'Green']])

print(myframe)
myframe.index.name = ['key1','key2']
myframe.columns.name = ['city','color']
print(myframe)