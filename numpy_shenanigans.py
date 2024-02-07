import numpy as np


a = np.random.randint(10, size=10)

a[0:5]

a[0] = 999

m = np.random.randint(10, size=(3,5))
m
m[1,1]
m[2,3] = 999

m[:,0]
m[1,:]
m[0:2,0:3]


v = np.arange(0,30,3)
v[1]
v[4]
v

catch=[1,2,3]
v[catch]

b = np.array([1,2,3,4,5])

ab = []
for i in b:
    print(i)


for i in b:  #boring not cool way
    if i <3:
        ab.append(i)
ab

w = np.array([1,2,3,4,5])   #fancy way
w<3
w[w<3] #bool ile check
w[w>3]
w[w!=3]
w[w==3]

w*5/10
v**3
v-2

np.subtract(w,1)
np.add(w,1)
np.mean(w)
np.sum(w)
np.min(w)
np.var(w)

#2 bilinmeyenli denklem

#5*x0 + x1 = 12
#x0 + 3*x1 = 10

a=np.array([[5,1],[1,3]])
b=np.array([12,10])

np.linalg.solve(a,b)




arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. dim 2.var: ', arr[0, 1])

arr

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
array = np.array([1, 2, 3, 4, 5, 6, 7])

