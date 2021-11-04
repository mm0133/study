import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh


# data read
fp_image = open('data/train-images.idx3-ubyte', 'rb')
fp_label = open('data/train-labels.idx1-ubyte', 'rb')
fp_image.read(16)
fp_label.read(8)
train_image = fp_image.read()
train_label = fp_label.read()

train_image = np.frombuffer(train_image, dtype='uint8').reshape(-1, 784)
train_label = np.frombuffer(train_label, dtype='uint8')
L=len(train_label)

fp_image = open('data/t10k-images.idx3-ubyte','rb')
fp_label = open('data/t10k-labels.idx1-ubyte','rb')
fp_image.read(16)
fp_label.read(8)
test_image=fp_image.read()
test_label=fp_label.read()

test_image = np.frombuffer(test_image, dtype='uint8').reshape(-1, 784)
test_label = np.frombuffer(test_label, dtype='uint8')
test_L=len(test_label)

class_n=10


# problem1 plot samples
x = train_image[:9]
x = x.reshape(9,28, 28)

fig = plt.figure()
for i in range(9):
    img=x[i]
    ax=fig.add_subplot(3,3,i+1)
    ax.imshow(img)
plt.show()
print("example image label:",train_label[:9])


#
tmp=np.sum(train_image,axis=0)
psi=tmp/L
A=train_image.copy()
A=A.astype(np.float64)
for i in range(len(A)):
    A[i]=A[i]-psi

C=np.matmul(A.T,A)
values, vectors = eigh(C)
values=np.flip(values, axis=0)
vectors=np.flip(vectors, axis=0)
sum_eig=np.sum(values)
threshold=0.95*sum_eig
tmp=0

K=len(values)
for i in range(len(values)):
    tmp+=values[i]
    if tmp>=threshold:
        K=i
        break
print('K coeff: {0}'.format(K))

u=vectors[:K]
W=np.matmul(A,u.T)
mean_w=np.zeros((class_n,K))
count=np.zeros(class_n)


for i in range(L):
    count[train_label[i]]+=1
    mean_w[train_label[i]]+=W[i]
for i in range(class_n):
    mean_w[i]/=count[i]


# 3
predict_label=np.zeros(test_label.shape, dtype='uint8')


A_test=test_image.copy()
A_test=A_test.astype(np.float64)
for i in range(test_L):
    A_test[i]=A_test[i]-psi

W_test=np.matmul(A_test,u.T)
for i in range(test_L):
    cl=0
    min_err=float('inf')
    for j in range(class_n):
        err=0
        for k in range(K):
            err+=(1/values[k])*(mean_w[j][k]-W_test[i][k])**2
        if err<min_err:
            cl=j
            min_err=err
    predict_label[i]=cl

answer=np.sum(predict_label==test_label)
accurate=answer*100/test_L
print('accurate: {0}%'.format(accurate))


# reconstructed=np.zeros((class_n,784))
# for i in range(class_n):
#     rec=psi
#     for j in range(K):
#         rec+=W[i][j]*u[k]
#     reconstructed[i]=rec
# reconstructed=reconstructed.reshape((class_n,28,28))
#
# fig = plt.figure()
# for i in range(10):
#     img=reconstructed[i]
#     ax=fig.add_subplot(2,5,i+1)
#     ax.imshow(img)
# plt.show()

