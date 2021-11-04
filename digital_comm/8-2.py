import numpy as np
from scipy import special
from matplotlib import pyplot as plt

np.random.seed(7777)
n_bit=10000
E=1
#N0 10*log(E/N0)=7 -> N0=0.1995
N0_array=np.arange(0.199,1.001,0.001)
error_prob_array=[]
for N0 in N0_array:
    S=np.random.rand(n_bit)

    n=np.random.normal(0,np.sqrt(N0/2),n_bit)
    small=S<0.5
    big=np.logical_not(small)

    y=np.sqrt(E*small)-np.sqrt(E*big)+n
    out_S=y>0
    error_prob_array.append(np.sum(out_S!=small)/n_bit)

x=10*np.log10(1/N0_array)
theory=0.5-0.5*special.erf(np.sqrt(2*E/N0_array)/np.sqrt(2))


plt.plot(x,theory,label='theory')
plt.scatter(x,error_prob_array,s=2,color='r',label='simulation')
plt.yscale("log")
plt.xlabel("SNR (dB)")
plt.ylabel("error_prob")
plt.legend()
plt.show()
