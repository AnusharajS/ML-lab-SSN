import numpy as np

n=int(input('Enter num of training data:'))
X=[]
print('Enter data row wise')
for i in range(2**n):         
    a =[]
    for j in range(n):      
         a.append(int(input()))
    X.append(a)
print(X)
epoch=int(input('Enter num of epochs:'))
b=1
target=[]

def AND(X,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==1 and inp[1]==1:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    wt_b=[0,0,0] #initial w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            wt_b[0]=wt_b[0]+(target[i]*inp[0])
            wt_b[1]=wt_b[1]+(target[i]*inp[1])
            wt_b[2]=wt_b[2]+(target[i])
        
            print(wt_b)
        print('\n')
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")

def OR(X,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==1 or inp[1]==1:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    wt_b=[0,0,0] #initial w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            wt_b[0]=wt_b[0]+(target[i]*inp[0])
            wt_b[1]=wt_b[1]+(target[i]*inp[1])
            wt_b[2]=wt_b[2]+(target[i])
        
            print(wt_b)
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")
def XOR(X,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==inp[1]:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    wt_b=[0,0,0] #initial w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            wt_b[0]=wt_b[0]+(target[i]*inp[0])
            wt_b[1]=wt_b[1]+(target[i]*inp[1])
            wt_b[2]=wt_b[2]+(target[i])
        
            print(wt_b)
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")

        
AND(X,b,epoch)

