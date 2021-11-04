import numpy as np
from matplotlib import pyplot as plt

np.random.seed(7777)
sigma_square=2
num_sample=10000

u_i=np.random.uniform(0,1,num_sample)
r_i=np.sqrt(2*sigma_square*np.log(1/(1-u_i)))
theta_i=np.random.uniform(0,2*np.pi,num_sample)
x_i=r_i*np.cos(theta_i)
y_i=r_i*np.sin(theta_i)

fig, axs = plt.subplots(2, 1)
cnt_x=axs[0].hist(x_i,bins=20, range=(-10,10))[0]
axs[0].set_title('X')
axs[0].set_ylabel('num_samples')
cnt_y=axs[1].hist(y_i,bins=20, range=(-10,10))[0]
axs[1].set_title('Y')
axs[1].set_ylabel('num_samples')

fig.show()
print('bins=20, range=(-10,10)')
print('count xi:',np.int64(cnt_x))
print('count yi:',np.int64(cnt_y))