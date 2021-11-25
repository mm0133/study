# -*- coding: utf-8 -*-
"""pattern_recognition_hw4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13sryxANfBbalfyCGvPl2yIjacuiSb1GP
"""

import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(123)
if device == 'cuda':
    torch.cuda.manual_seed_all(123)


learning_rate = 0.001
training_epochs = 15
batch_size = 100
val_size=6000



class A_CNN(torch.nn.Module):
    def __init__(self):
        super(A_CNN, self).__init__()
        self.name='A_Network'
        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=3, stride=1, padding='valid'),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding='valid'),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

        self.layer3=torch.nn.Sequential(
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding='valid'),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))


        self.fc = torch.nn.Linear(1600, 10, bias=True)
        # torch.nn.init.xavier_uniform_(self.fc.weight)
        # torch.nn.init.normal_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)    #cov2d, Relu, maxpool
        out = self.layer2(out) #cov2d, Relu, maxpool
        out = out.view(out.size(0), -1)   #  Flatten
        out = self.fc(out)  #dense
        return out


class B_CNN(torch.nn.Module):
    def __init__(self):
        super(B_CNN, self).__init__()
        self.name='B_Network'
        self.layer1= torch.nn.Sequential(
            torch.nn.Conv2d(1,16,kernel_size=3,stride=1,padding='same'),
            torch.nn.ReLU(),
            torch.nn.Conv2d(16,16,kernel_size=3,stride=1,padding='same'),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2,stride=2)
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=3, stride=1, padding='valid'),
            torch.nn.ReLU(),
            torch.nn.Conv2d(32, 32, kernel_size=3, stride=1, padding='valid'),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.fc = torch.nn.Linear(800, 10, bias=True)
        # torch.nn.init.xavier_uniform_(self.fc.weight)
        # torch.nn.init.normal_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)  # cov2d, Relu, cov2d, Relu, maxpool
        out = self.layer2(out) # cov2d, Relu, cov2d, Relu, maxpool
        out = out.view(out.size(0), -1)  # Flatten
        out = self.fc(out) #Dense
        return out

class Train_result:
  def __init__(self,train_cost_list,val_cost_list,val_accuracy):
    self.train_cost=train_cost_list
    self.val_cost=val_cost_list
    self.val_accuracy=val_accuracy


def train_model(model):

    train_cost_list=[]
    val_cost_list=[]
    val_accuracy_list=[]
    criterion = torch.nn.CrossEntropyLoss().to(device)    # softmax + cross entropy
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    print(f'\n{model.name} start.')
    for epoch in range(training_epochs):
        avg_cost_train = 0
        for X, Y in data_loader:
            X = X.to(device)
            Y = Y.to(device)

            optimizer.zero_grad()
            hypothesis = model(X)
            cost = criterion(hypothesis, Y)
            cost.backward()
            optimizer.step()
            avg_cost_train += cost / total_batch
        with torch.no_grad():
          prediction = model(val_X)
          avg_cost_val=criterion(prediction, val_Y)
          correct_prediction = torch.argmax(prediction, 1) == val_Y
          val_accuracy = correct_prediction.float().mean()*100
        train_cost_list.append(avg_cost_train)
        val_cost_list.append(avg_cost_val)
        val_accuracy_list.append(val_accuracy)
        print(f'Epoch: {epoch + 1:3d}, train_cost: {avg_cost_train:.9f}, val_cost:{avg_cost_val:.9f}, val_accuracy:{val_accuracy}')
    return Train_result(train_cost_list,val_cost_list,val_accuracy_list)

mnist_train = dsets.MNIST(root='./data',
                          train=True,
                          transform=transforms.ToTensor(),
                          download=True)

train_set, val_set = torch.utils.data.random_split(mnist_train, [60000-val_size, val_size])

test_set = dsets.MNIST(root='./data',
                         train=False,
                         transform=transforms.ToTensor(),
                         download=True)


val_dataloader = torch.utils.data.DataLoader(dataset=val_set, batch_size=6000)
test_X= test_set.test_data.view(-1, 1, 28, 28).float().to(device)
test_Y=test_set.test_labels.to(device)
val_X, val_Y = next(iter(val_dataloader))

val_X=val_X.view(-1, 1, 28, 28).float().to(device)
val_Y=val_Y.to(device)

data_loader = torch.utils.data.DataLoader(dataset=train_set,
                                          batch_size=batch_size,
                                          shuffle=True,
                                          drop_last=True)

total_batch = len(data_loader)
model_A=A_CNN().to(device)
model_B=B_CNN().to(device)

result_A=train_model(model_A)
result_B=train_model(model_B)

epoch_line=[i for i in range(1,training_epochs+1)]
plt.subplots(figsize=(12,4))
plt.tight_layout()
plt.subplot(1,3,1)
plt.plot(epoch_line,result_A.val_accuracy,label='A val_set accuracy')
plt.plot(epoch_line,result_B.val_accuracy,label='B val_set accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.title('accuracy comparison')
plt.legend()
plt.subplot(1,3,2)
plt.plot(epoch_line,result_A.val_cost,label='A val_cost')
plt.plot(epoch_line,result_A.train_cost,label='A train_cost')
plt.ylabel('cost')
plt.xlabel('epoch')
plt.title('A network cost')
plt.legend()
plt.subplot(1,3,3)
plt.plot(epoch_line,result_B.val_cost,label='B val_cost')
plt.plot(epoch_line,result_B.train_cost,label='B train_cost')
plt.ylabel('cost')
plt.xlabel('epoch')
plt.title('B network cost')
plt.legend()
plt.show()

with torch.no_grad():
    prediction = model_A(test_X)
    correct_prediction = torch.argmax(prediction, 1) == test_Y
    A_test_acc = correct_prediction.float().mean()*100

    prediction = model_B(test_X)
    correct_prediction = torch.argmax(prediction, 1) == test_Y
    B_test_acc = correct_prediction.float().mean()*100

print(f'A test accuracy: {A_test_acc:.6f} , B test accuracy:{B_test_acc:.6f}')