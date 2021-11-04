import numpy as np
from matplotlib import pyplot as plt

np.random.seed(7777)
sigma_array=[0.1,0.3,0.5]
result=[]
n_samples=100
E=1

for sigma in sigma_array:
    S = np.random.rand(n_samples)
    n0=np.random.normal(0,sigma,n_samples)
    n1 = np.random.normal(0, sigma, n_samples)
    small=S<0.5
    big=np.logical_not(small)
    y0=np.sqrt(E*small)+n0
    y1=np.sqrt(E*big)+n1
    result.append((y0[small],y1[small],y0[big],y1[big]))


plt.subplots(constrained_layout=True)
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.axvline(x=0, color='black', linewidth=1)
    plt.axhline(y=0, color='black', linewidth=1)
    plt.title(f'sigma={sigma_array[i]}')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.scatter(result[i][0],result[i][1],s=2,label='0')
    plt.scatter(result[i][2], result[i][3], s=2, label='1')
    plt.legend()
plt.show()


