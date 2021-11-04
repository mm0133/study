from scipy import io
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import numpy as np

# problem1 Data visualization
class1=io.loadmat('data/class1.mat')['R']
class2=io.loadmat('data/class2.mat')['R']
observation=io.loadmat('data/observation.mat')['obs']

plt.plot(class1[:,0],class1[:,1],"o",color="red",label="class1")
plt.plot(class2[:,0],class2[:,1],"o",color="blue", label="class2")
plt.plot(observation[:,0],observation[:,1],"o",color="green", label="observation", alpha=0.8)
plt.xlabel("length")
plt.ylabel("weight")
plt.legend()
plt.show()


# problem2 Data statistics
mean1=np.mean(class1,axis=0)
cov1=np.cov(class1.T)
mean2=np.mean(class2, axis=0)
cov2=np.cov(class2.T)
print('mean of class1\n',mean1)
print('covariance of class1\n',cov1,'\n')
print('mean of class2\n',mean2)
print('covariance of class2\n',cov2)


# problem3 Data prediction
def get_predicttion(p1, p2, obs_data):
    predict=[]
    likelihood=[]
    for fish in obs_data:
        l1,l2=p1.pdf(fish), p2.pdf(fish)
        if l1 > l2:
            predict.append(1)
        else:
            predict.append(2)
        likelihood.append([l1,l2])
    return np.array(predict),np.array(likelihood)

p1=multivariate_normal(mean=mean1,cov=cov1)
p2=multivariate_normal(mean=mean2,cov=cov2)
multi_predict, multi_likelihood=get_predicttion(p1,p2,observation)
print('\n\nlikelihood using two features\n',multi_likelihood)
print('prediction using two features\n',multi_predict)


p1=multivariate_normal(mean=mean1[0],cov=cov1[0][0])
p2=multivariate_normal(mean=mean2[0],cov=cov2[0][0])
length_predict, length_likelihood=get_predicttion(p1,p2,observation[:,0])
print('\n\nlikelihood using only length\n',length_likelihood)
print('prediction using only length\n',length_predict)

p1=multivariate_normal(mean=mean1[1],cov=cov1[1][1])
p2=multivariate_normal(mean=mean2[1],cov=cov2[1][1])
weight_predict, weight_likelihood=get_predicttion(p1,p2,observation[:,1])
print('\n\nlikelihood using only weight\n',weight_likelihood)
print('prediction using only weight\n',weight_predict)
