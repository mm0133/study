import numpy as np
from matplotlib import pyplot as plt

np.random.seed(7777)
Ui=np.random.uniform(0,1,10000)
Xi=2*Ui**0.5
cnt=plt.hist(Xi,bins=20, range=(0,2))[0]
print("count for each bin:",cnt)
plt.show()

